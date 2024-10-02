from django.shortcuts import render,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost

class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blogpost_list.html'

class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'blogpost_detail.html'

class BlogPostCreateView(CreateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('blogpost_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    template_name = 'blogpost_form.html'
    fields = ['title', 'content']

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blogpost_confirm_delete.html'
    success_url = reverse_lazy('blogpost_list')

