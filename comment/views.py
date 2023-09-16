from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import View

from post.models import Post
from .models import Comment
from .forms import CreateCommentForm


class CreateCommentView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        form = CreateCommentForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Comment.objects.create(
                user=request.user,
                post=post,
                body=cd['body'],
            )
        return redirect('home:home')
