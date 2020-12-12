from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db import transaction
from django.shortcuts import render, redirect
from rx.forms import CreateRxForm, EditRxForm, OnHoldFormCreate
from rx.models import Rx, OnHold

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


def get_user_rx_collection(request):
    user = request.user
    clients_group = Group.objects.get(name='Clients')
    if clients_group in user.groups.all():
        rxs = Rx.objects.filter(user_id=user.id).order_by('-id')
    else:
        rxs = Rx.objects.all().order_by('-id')

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
    rxs = get_user_rx_collection(request)
    context = {
        'rxs': rxs,
        'form': CreateRxForm(),
    }
    if pk:
        edit_form = get_prefilled_edit_form(pk)
        context['edit_form'] = edit_form
        context['pk'] = pk

    return context


@login_required
def user_workflow(request, pk=None):
    if request.method != 'POST':

        context = profile_get(request, pk)
        return render(request, 'shared/user_workflow.html', context)
    else:
        rx = Rx.objects.get(pk=pk)
        image = rx.image
        if not request.FILES:
            request.FILES['image'] = image
        form = EditRxForm(request.POST, request.FILES, initial=rx.__dict__)
        form.full_clean()

        if form.is_valid():
            update_rx(rx, form)
            return redirect('current user profile')
        else:
            rxs = get_user_rx_collection(request)

            context = {
                'rxs': rxs,
                'form': CreateRxForm(),
                'edit_form': form,
                'pk': pk
            }
            return render(request, 'shared/user_workflow.html', context)


def list_rx(request):
    user = request.user
    rxs = Rx.objects.filter(user_id=user.id).order_by('id')
    for rx in rxs:
        rx.status = STATUS_CHOICES[rx.status]

    context = {
        'rxs': rxs,
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
        form_on_hold = OnHoldFormCreate()
        context = {
            'rx': rx,
            'form': form,
            'form_on_hold': form_on_hold,
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


def create_status_modulator(request, instance, form, rx):
    if form.is_valid():
        instance.comment = form.cleaned_data['comment']
        instance.rx = rx
        instance.user = request.user
        instance.save()

@login_required()
def on_hold_create(request, pk):
    rx = Rx.objects.get(pk=pk)
    form = OnHoldFormCreate(request.POST)
    onhold = OnHold()
    create_status_modulator(request, onhold, form, rx)
    rx.status = 'H'
    rx.save()

    return redirect('list rx')

@login_required()
def on_hold_delete(request, pk):
    onhold = OnHold.objects.get(pk=pk)
    if onhold.user != request.user:
        # TODO -> let the manager delete onholds
        # TODO -> forbid and presentation
        pass
    onhold.delete()
    return redirect('current user profile')


