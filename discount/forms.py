from django import forms

from discount.models import CsvFile


class CurrentFileUploadForm(forms.ModelForm):
    class Meta:
        model = CsvFile
        fields = '__all__'
