from django.shortcuts import render, redirect

# Create your views here.
from rx.forms import CreateRxForm, EditRxForm
from rx.models import Rx


def list_rx(request):
    rxs = Rx.objects.all().order_by('id')
    status_choices = {
        'A': 'Active',
        'H': 'On Hold',
        'P': 'Prepared',
        'R': 'Ready For Pick-up',
        'F': 'Finished',

    }
    for rx in rxs:
        rx.status = status_choices[rx.status]

    context = {
        'rxs': rxs
    }
    return render(request, 'list.html', context)


def create_rx(request):
    if request.method == "GET":
        context = {
            'form': CreateRxForm()
        }
        return render(request, 'create.html', context)

    else:
        form = CreateRxForm(request.POST, request.FILES)
        # form.data['status'] = 'A'

        if form.is_valid():
            # form.save()
            rx = Rx(**form.cleaned_data)
            rx.save()
            return redirect('list rx')
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
            'form': form
        }
        return render(request, 'edit.html', context)
    else:
        image = rx.image
        if not request.FILES:
            request.FILES['image'] = image
        form = EditRxForm(request.POST, request.FILES)

        if form.is_valid():
            rx.first_name = form.cleaned_data['first_name']
            rx.last_name = form.cleaned_data['last_name']
            rx.age = form.cleaned_data['age']
            rx.status = form.cleaned_data['status']
            rx.image = form.cleaned_data['image']
            # form.save()
            # rx = Rx(**form.cleaned_data)
            rx.save()
            return redirect('list rx')
        else:
            context = {
                'form': form,
                'form_errors': form.errors,
            }
            return render(request, 'edit.html', context)
