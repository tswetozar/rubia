from django.urls import path

from common.views import index
from rx.views import list_rx, create_rx, edit_rx, user_workflow, on_hold_create, on_hold_delete

urlpatterns = (
    path('', list_rx, name='list rx'),
    path('workflow/', user_workflow, name='current user profile'),
    path('workflow/<int:pk>/', user_workflow, name='user profile'),
    path('create/', create_rx, name='create rx'),
    path('edit/<int:pk>', edit_rx, name='edit rx'),
    path('onhold/<int:pk>', on_hold_create, name='on hold rx'),
    path('onhold/delete/<int:pk>', on_hold_delete, name='delete on hold'),
)
