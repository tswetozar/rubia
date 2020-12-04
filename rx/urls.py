from django.urls import path

from common.views import index
from rx.views import list_rx, create_rx, edit_rx

urlpatterns = (
    path('', list_rx, name='list rx'),
    path('create/', create_rx, name='create rx'),
    path('edit/<int:pk>', edit_rx, name='edit rx')
)