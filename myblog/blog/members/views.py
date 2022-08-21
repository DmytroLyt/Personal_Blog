from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SingUpForm, EditProfileForm, PasswordChange

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChange
    #form_class = PasswordChangeForm
    success_url = reverse_lazy('password_changed')
    #success_url = reverse_lazy('home')

def password_changed(request):
    return render(request, 'registration/password_changed.html', {})

class UserRegister(generic.CreateView):
    form_class = SingUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEdit(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
