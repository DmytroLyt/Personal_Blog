from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SingUpForm, EditProfileForm, PasswordChange, ProfilePageForm
from myblog.models import User_Profile


class CreateProfilePageView(CreateView):
    model = User_Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_user_page.html'

    # fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class EditProfilePageView(generic.UpdateView):
    model = User_Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'github_url', 'linkedin_url']
    success_url = reverse_lazy('home')


class ProfilePageView(DetailView):
    model = User_Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        user_page = User_Profile.objects.all()
        context = super(ProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(User_Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChange
    # form_class = PasswordChangeForm
    success_url = reverse_lazy('password_changed')
    # success_url = reverse_lazy('home')


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
