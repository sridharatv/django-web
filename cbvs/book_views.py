from django.shortcuts import render
from django.views.generic import (View,
                                  CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import  LoginRequiredMixin
from . import models

# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    # by default ListView returns book_list context dict.
    # changing that to 'libraries'
    context_object_name = 'books'
    model = models.Book
    login_url = '/login/login/'
    redirect_field_name = 'cbvs/book_list.html'

class BookDetailView(LoginRequiredMixin, DeleteView):
    # by default DetailView returns 'book' context dict
    # changing that to 'book_detail'
    context_object_name = 'book_detail'
    model = models.Book
    template_name = 'cbvs/book_detail.html'
    login_url = '/login/login/'
    redirect_field_name = 'cbvs/book_detail.html'

class BookCreateView(LoginRequiredMixin, CreateView):
    model = models.Book
    fields = '__all__'
    login_url = '/login/login/'
    redirect_field_name = 'cbvs/book_list.html'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    model = models.Book
    fields = '__all__'
    login_url = '/login/login'
    redirect_field_name = 'cbvs/book_list.html'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Book
    success_url = reverse_lazy("cbvs:book_list")
    login_url = '/login/login/'
    redirect_field_name = 'cbvs/book_list.html'




