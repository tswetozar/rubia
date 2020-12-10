from django.urls import path, include

from accounts.views import user_profile, signup_user, sign_out_user

urlpatterns = [
    # path('signin/', LoginView.as_view(template_name='registration/login.html', name='signin user')),
    path('profile/', user_profile, name='current user profile'),
    path('profile/<int:pk>/', user_profile, name='user profile'),
    path('signup/', signup_user, name='signup user'),
    path('signout/', sign_out_user, name='sign out user')
]