from django.urls import path

from common.views import index
from rx.views import list_rx, create_rx, edit_rx, user_workflow, on_hold_create, on_hold_delete, prepared_create, \
    prepared_delete, ready_create, ready_delete, finished_create, finished_delete, delete_rx

urlpatterns = (
    path('', list_rx, name='list rx'),
    path('workflow/', user_workflow, name='current user profile'),
    path('workflow/<int:pk>/', user_workflow, name='user profile'),

    path('create/', create_rx, name='create rx'),
    path('edit/<int:pk>', edit_rx, name='edit rx'),
    path('delete/<int:pk>', delete_rx, name='delete rx'),

    path('onhold/<int:pk>', on_hold_create, name='on hold rx'),
    path('onhold/delete/<int:pk>', on_hold_delete, name='delete on hold'),

    path('prepared/<int:pk>', prepared_create, name='prepared rx'),
    path('prepared/delete/<int:pk>', prepared_delete, name='delete prepared'),

    path('ready/<int:pk>', ready_create, name='ready rx'),
    path('ready/delete/<int:pk>', ready_delete, name='delete ready'),

    path('finished/<int:pk>', finished_create, name='finished rx'),
    path('finished/delete/<int:pk>', finished_delete, name='delete finished'),
)
