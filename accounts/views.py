from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import views as auth_views

from .forms import UserRegisterForm, UserEditProfileForm
from .models import Profile, Relation


class UserRegisterView(CreateView):
    form_class = UserRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('accounts:user_login')


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('home:home')


class UserLogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('home:home')


class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, pk):
        is_following = False
        user = get_object_or_404(User, id=pk)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists():
            is_following = True
        return render(request, 'accounts/profile.html', context={'user': user, 'is_following': is_following})


class UserEditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = UserEditProfileForm
    template_name = 'accounts/edit_profile.html'

    def get_initial(self):
        initial_data = super().get_initial()
        initial_data['username'] = self.request.user.username
        initial_data['email'] = self.request.user.email
        return initial_data

    def form_valid(self, form):
        user = get_object_or_404(User, id=self.kwargs['pk'])
        if form.is_valid():
            form.save()
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accounts:user_profile', kwargs={'pk': self.kwargs['pk']})


class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if not relation.exists() and (user != request.user):
            Relation.objects.create(from_user=request.user, to_user=user)
        return redirect(request.META.get('HTTP_REFERER'))


class UserUnfollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)
        if relation.exists() and (user != request.user):
            relation.delete()
        return redirect(request.META.get('HTTP_REFERER'))
