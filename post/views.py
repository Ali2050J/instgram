from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from .models import Post, Save


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('image', 'caption', 'status')
    template_name = 'post/post_create.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        new_post = form.save(commit=False)
        new_post.user = self.request.user
        new_post.save()
        return super().form_valid(form)


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ('image', 'caption', 'status')
    template_name = 'post/post_edit.html'
    success_url = reverse_lazy('home:home')


class PostLikeView(LoginRequiredMixin, View):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        if not (request.user in post.like.all()):
            post.like.add(request.user)
        else:
            post.like.remove(request.user)
        return redirect('home:home')


class SavePostView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        post = Post.objects.get(pk=pk)
        save = Save.objects.get(user=user)
        if post not in save.post.all():
            save.post.add(post)
        return redirect(request.META.get('HTTP_REFERER'))


class UnSavePostView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = request.user
        post = Post.objects.get(pk=pk)
        save = Save.objects.get(user=user)
        if post in save.post.all():
            save.post.remove(post)
        return redirect(request.META.get('HTTP_REFERER'))
