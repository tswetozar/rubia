from os.path import join, isfile

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.clean_up import clean_up_files
from core.update_profiles import update_profiles
from discount.forms import CurrentFileUploadForm
from discount.models import CsvFile
from rubia import settings


def current_file(request):
    discount_file = CsvFile.objects.all().order_by('id').reverse()[0]
    if request.method == 'GET':
        context = {
            'file': discount_file,
            'form': CurrentFileUploadForm()
        }
        return render(request, 'discount_create.html', context)
    else:
        old_file = discount_file
        form = CurrentFileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            discount_file = CsvFile.objects.all().order_by('id').reverse()[0]
            update_profiles(discount_file.csv_file.path)
            return redirect('list rx')
        else:
            context = {
                'file': discount_file,
                'form': form
            }
            return render(request, 'discount_create.html', context)


def get_private_file(request, path_to_file):
    if isfile(path_to_file):
        has_access = True
        file = open(path_to_file, 'rb')
        response = HttpResponse(content=file)
        response['Content-Disposition'] = 'attachment'
        return response
    else:
        return None
