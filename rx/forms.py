from django import forms

from rx.models import Rx


class EditRxForm(forms.Form):

    STATUS_CHOICES = (
        ('A', 'Active'),
        ('H', 'On Hold'),
        ('P', 'Prepared'),
        ('R', 'Ready For Pick-up'),
        ('F', 'Finished'),
    )

    first_name = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'id': 'first_name_id',
                'type': 'text',
                'class': 'validate',
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'id': 'last_name_id',
                'type': 'text',
                'class': 'validate',
            }
        )
    )
    age = forms.IntegerField(
        min_value=0,
        max_value=130,
        label='',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Age',
                'id': 'age_id',
                'type': 'text',
                'class': 'validate',
            }
        )
    )
    status = forms.ChoiceField(
        choices=STATUS_CHOICES,
    )
    image = forms.ImageField(
        widget=forms.FileInput(
        )
    )


class CreateRxForm(forms.Form):

    STATUS_CHOICES = (
        ('A', 'Active'),
        ('H', 'On Hold'),
        ('P', 'Prepared'),
        ('R', 'Ready For Pick-up'),
        ('F', 'Finished'),
    )

    first_name = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                'id': 'first_name_id',
                'type': 'text',
                'class': 'validate',
            }
        )
    )
    last_name = forms.CharField(
        max_length=30,
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'id': 'last_name_id',
                'type': 'text',
                'class': 'validate',
            }
        )
    )
    age = forms.IntegerField(
        min_value=0,
        max_value=130,
        label='',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Age',
                'id': 'age_id',
                'type': 'text',
                'class': 'validate',
            }
        )
    )
    image = forms.ImageField(
        widget=forms.FileInput(
        )
    )
