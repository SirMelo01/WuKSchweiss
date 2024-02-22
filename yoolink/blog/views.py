from django.shortcuts import render
from django.views.generic import ListView, DetailView
from yoolink.views import get_opening_hours
from yoolink.ycms.models import Blog


class Load_Index_Blog(ListView):
    model = Blog
    template_name = 'blog/index_blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_opening_hours())
        return context

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_opening_hours())
        return context