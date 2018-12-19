from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = ['title', 'body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(CreateView, self).form_valid(form)

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_edit.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')
