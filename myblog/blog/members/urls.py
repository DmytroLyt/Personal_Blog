from django.urls import path
from .views import UserRegister, UserEdit, PasswordsChangeView, ProfilePageView, EditProfilePageView, \
    CreateProfilePageView
# from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', UserRegister.as_view(), name='register'),
    path('edit_profile/', UserEdit.as_view(), name='edit_profile'),
    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
    path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
    path('password_changed', views.password_changed, name="password_changed"),
    path('<int:pk>/user_profile/', ProfilePageView.as_view(), name='profile_page'),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
    path('create_profile_page/', CreateProfilePageView.as_view(), name='create_profile_page'),

]
