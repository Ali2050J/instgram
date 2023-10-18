from django.contrib.auth.models import User
from django.views.generic import ListView

from post.models import Post


class HomeView(ListView):
    template_name = 'home/index.html'
    queryset = Post.objects.select_related('user').select_related('user__profile').prefetch_related('comments').filter(status='publish')
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['users'] = User.objects.select_related('profile').all()
        return context
