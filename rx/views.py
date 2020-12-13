from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db import transaction
from django.shortcuts import render, redirect
from rx.forms import CreateRxForm, EditRxForm, StatusModifierCreateForm, FilterForm
from rx.models import Rx, OnHold, Prepared, Ready, Finished

STATUS_CHOICES = {
    'A': 'Active',
    'H': 'On Hold',
    'P': 'Prepared',
    'R': 'Ready For Pick-up',
    'F': 'Finished',

}


def get_prefilled_edit_form(pk):
    rx_edit = Rx.objects.get(pk=pk)
    edit_form = EditRxForm(initial=rx_edit.__dict__)

    return edit_form


def extract_filter_values(params):
    order = params['order'] if 'order' in params else FilterForm.ORDER_ASC
    text = params['text'] if 'text' in params else ''

    return {'order': order, 'text': text}


def get_user_rx_collection(request):
    user = request.user
    clients_group = Group.objects.get(name='Clients')
    if clients_group in user.groups.all():
        rxs = Rx.objects.filter(user_id=user.id).order_by('-id')
    else:
        params = extract_filter_values(request.GET)
        order_by = 'id' if params['order'] == FilterForm.ORDER_ASC else '-id'
        rxs = Rx.objects.filter(first_name__icontains=params['text']).order_by(order_by)
        # rxs = Rx.objects.all().order_by('-id')

    for rx in rxs:
        rx.status = STATUS_CHOICES[rx.status]

    return rxs


def update_rx(rx, form):
    rx.first_name = form.cleaned_data['first_name']
    rx.last_name = form.cleaned_data['last_name']
    rx.age = form.cleaned_data['age']
    rx.status = form.cleaned_data['status']
    rx.image = form.cleaned_data['image']
    rx.save()


def profile_get(request, pk):
    filter_params = extract_filter_values(request.GET)
    rxs = get_user_rx_collection(request)
    context = {
        'rxs': rxs,
        'form': CreateRxForm(),
        'form_on_hold': StatusModifierCreateForm(),
        'form_prepared': StatusModifierCreateForm(),
        'form_ready': StatusModifierCreateForm(),
        'form_finished': StatusModifierCreateForm(),
        'filter_form': FilterForm(initial=filter_params)
    }
    if pk:
        edit_form = get_prefilled_edit_form(pk)
        context['edit_form'] = edit_form
        context['pk'] = pk

    return context


@login_required
def user_workflow(request, pk=None, errors=None):
    filter_params = extract_filter_values(request.GET)
    if request.method != 'POST':

        context = profile_get(request, pk)
        context['errors'] = errors
        return render(request, 'shared/user_workflow.html', context)
    else:
        # rx = Rx.objects.get(pk=pk)
        # image = rx.image
        # if not request.FILES:
        #     request.FILES['image'] = image
        # form = EditRxForm(request.POST, request.FILES, initial=rx.__dict__)
        # form.full_clean()
        #
        # if form.is_valid():
        #     update_rx(rx, form)
        #     return redirect('current user profile')
        # else:
        rxs = get_user_rx_collection(request)

        context = {
            'rxs': rxs,
            'form': CreateRxForm(),
            # 'edit_form': form,
            'pk': pk,
                'filter_form': FilterForm(initial=filter_params)
        }
        return render(request, 'shared/user_workflow.html', context)


def list_rx(request):
    params = extract_filter_values(request.GET)
    order_by = 'first_name' if params['order'] == FilterForm.ORDER_ASC else '-first_name'
    rxs = Rx.objects.filter(first_name__icontains=params['text']).order_by(order_by)

    # user = request.user
    # rxs = Rx.objects.all().ordered_by('-id')
    # rxs = Rx.objects.filter(user_id=user.id).order_by('id')
    for rx in rxs:
        rx.status = STATUS_CHOICES[rx.status]

    context = {
        'rxs': rxs,
        'filter_form': FilterForm(initial=params)
    }
    return render(request, 'list.html', context)


@transaction.atomic
def create_rx(request):
    if request.method == "GET":
        context = {
            'form': CreateRxForm()
        }
        return render(request, 'create.html', context)

    else:
        form = CreateRxForm(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            form.full_clean()
            rx = Rx(**form.cleaned_data)
            rx.user = user
            rx.save()
            return redirect('current user profile')
        else:
            context = {
                'form': form
            }
            return render(request, 'create.html', context)


def edit_rx(request, pk):
    rx = Rx.objects.get(pk=pk)

    if request.method == 'GET':
        form = EditRxForm(initial=rx.__dict__)
        context = {
            'rx': rx,
            'form': form,
            'form_on_hold': StatusModifierCreateForm(),
            'form_prepared': StatusModifierCreateForm(),
            'form_ready': StatusModifierCreateForm(),
            'form_finished': StatusModifierCreateForm(),
        }
        return render(request, 'edit.html', context)
    else:
        image = rx.image
        if not request.FILES:
            request.FILES['image'] = image
        form = EditRxForm(request.POST, request.FILES, initial=rx.__dict__)
        form.full_clean()

        if form.is_valid():
            update_rx(rx, form)
            return redirect('list rx')
        else:
            context = {
                'form': form,
                'form_errors': form.errors,
            }
            return render(request, 'edit.html', context)


def delete_rx(request, pk):
    rx = Rx.objects.get(pk=pk)
    if rx.user != request.user:
        errors = "You cant delete other ppl stuff"
        return user_workflow(request, pk=None, errors=errors)
    if request.method == "GET":
        context = {
            'rx': rx,
        }

        return render(request, 'partials/confirm_delete.html', context)
    else:
        rx.delete()
        return redirect('current user profile')


def create_status_modulator(request, pk, model, status):
    rx = Rx.objects.get(pk=pk)
    form = StatusModifierCreateForm(request.POST)
    instance = model()
    if form.is_valid():
        instance.comment = form.cleaned_data['comment']
        instance.rx = rx
        instance.user = request.user
        instance.save()
        rx.status = status
        rx.save()


def delete_status_modifier(request, pk, model):
    item = model.objects.get(pk=pk)
    if item.user != request.user:
        # TODO -> let the manager delete item
        # TODO -> forbid and presentation
        errors = "You cant delete other ppl stuff"
        return user_workflow(request, pk=None, errors=errors)
    else:
        item.delete()
        return redirect('current user profile')


@login_required()
def on_hold_create(request, pk):
    create_status_modulator(request, pk, OnHold, 'H')
    return redirect('list rx')


@login_required()
def on_hold_delete(request, pk):
    return delete_status_modifier(request, pk, OnHold)


def prepared_create(request, pk):
    create_status_modulator(request, pk, Prepared, 'P')
    return redirect('list rx')


def prepared_delete(request, pk):
    return delete_status_modifier(request, pk, Prepared)


def ready_create(request, pk):
    create_status_modulator(request, pk, Ready, 'R')
    return redirect('list rx')


def ready_delete(request, pk):
    return delete_status_modifier(request, pk, Ready)


def finished_create(request, pk):
    create_status_modulator(request, pk, Finished, 'F')
    return redirect('list rx')


def finished_delete(request, pk):
    return delete_status_modifier(request, pk, Finished)
