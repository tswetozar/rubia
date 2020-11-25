from django.shortcuts import render, redirect

# Create your views here.
from rx.forms import RxForm
from rx.models import Rx


def list_rx(request):
    rxs = Rx.objects.all()
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
            'form': RxForm()
        }
        return render(request, 'create.html', context)

    else:
        form = RxForm(request.POST)

        if form.is_valid():
            # form.save()
            rx = Rx(**form.cleaned_data)
            rx.save()
            return redirect('list rx')


def edit_rx(request):
    return render(request, 'edit.html')
