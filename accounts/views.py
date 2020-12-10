from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from accounts.forms import CustomUserCreationForm
from accounts.models import UserProfile
from rx.forms import CreateRxForm, EditRxForm
from rx.models import Rx


def user_profile(request, pk=None):
    if request.method != 'POST':
        if pk:
            rx_edit = Rx.objects.get(pk=pk)
            edit_form = EditRxForm(initial=rx_edit.__dict__)

        user = request.user
        rxs = Rx.objects.filter(user_id=user.id).order_by('-id')
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
            'rxs': rxs,
            'form': CreateRxForm(),
        }
        if pk:
            context['edit_form'] = edit_form
            context['pk'] = pk
        return render(request, 'registration/user_profile.html', context)
    else:
        rx = Rx.objects.get(pk=pk)
        image = rx.image
        if not request.FILES:
            request.FILES['image'] = image
        form = EditRxForm(request.POST, request.FILES, initial=rx.__dict__)
        form.full_clean()

        if form.is_valid():
            rx.first_name = form.cleaned_data['first_name']
            rx.last_name = form.cleaned_data['last_name']
            rx.age = form.cleaned_data['age']
            rx.status = form.cleaned_data['status']
            rx.image = form.cleaned_data['image']
            rx.save()
            return redirect('current user profile')
        else:
            if pk:
                rx_edit = Rx.objects.get(pk=pk)
                edit_form = EditRxForm(initial=rx_edit.__dict__)

            user = request.user
            rxs = Rx.objects.filter(user_id=user.id).order_by('-id')
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
                'rxs': rxs,
                'form': CreateRxForm(),
            }
            if pk:
                context['edit_form'] = edit_form
                context['pk'] = pk
            return render(request, 'registration/user_profile.html', context)



def signup_user(request):
    if request.method == "GET":
        context = {
            'form': CustomUserCreationForm(),
        }
        return render(request, 'registration/registration.html', context)
    else:
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserProfile(
                user=user
            )
            profile.save()
            return redirect('common index')


def sign_out_user(request):
    logout(request)
    return redirect('common index')
