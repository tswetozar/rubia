from django import forms

from rx.models import Rx


class RxForm(forms.Form):
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
                'id': 'last_name_id',
                'type': 'text',
                'class': 'validate',
            }
        )
    )


    # class Meta:
    #     model = Rx
    #     fields = '__all__'
    #     widgets = {
    #         'first_name': forms.TextInput(
    #             attrs={
    #                 'placeholder': 'First Name',
    #                 'id': 'first_name_id',
    #                 'type': 'text',
    #                 'class': 'validate',
    #             }
    #         )
    #    }
