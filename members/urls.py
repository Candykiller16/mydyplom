from django import views
from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView, CreateProfilePage
# from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
        path('register/', UserRegisterView.as_view(), name='register'), # <!-- Нам не нужно прописывать url для logout, т.к. она уже прописана в django.auto -->
        path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
        # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change-password.html')),
        path('password/', PasswordsChangeView.as_view(template_name='registration/change-password.html')),
        path('password_success', views.password_success, name='password_success'),
        path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
        path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
        path('create_profile_page/', CreateProfilePage.as_view(), name='create_profile_page'),


]