from django.shortcuts import render
from django.views.generic import *
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from rest_framework.exceptions import PermissionDenied

class NewsListView(ListView):
    model = Post
    template_name = 'home.html'


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news/post_detail.html'

class NewsCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'news.add_post'
    model = Post
    template_name = 'news/post_new.html'
    fields = ['title', 'author', 'body']

    def add_post(request):
        # Проверяем есть ли у данного пользователя разрешение для добавления поста
        # Если такого разрешения нет, то выкидываем исключение PermissionDenied
        if not request.user.has_perm('news.add_post'):
            raise PermissionDenied

class NewsUpdateView(UpdateView):  # Новый класс
    model = Post
    template_name = 'news/post_edit.html'
    fields = ['title', 'body']

class NewsDeleteView(DeleteView): # Создание нового класса
    model = Post
    template_name = 'news/post_delete.html'
    success_url = reverse_lazy('home')


