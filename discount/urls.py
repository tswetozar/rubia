from django.urls import path

from discount.views import current_file, get_private_file

urlpatterns = (
    path('', current_file, name='current file'),
    path('/<path:path_to_file>', get_private_file, name='get private file')
)