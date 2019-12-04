from django.shortcuts import render
from django.views.generic import (View,
                                  CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from django.urls import reverse, reverse_lazy
from . import models

# Create your views here.

class BookListView(ListView):
    # by default ListView returns book_list context dict.
    # changing that to 'libraries'
    context_object_name = 'books'
    model = models.Book

class BookDetailView(DeleteView):
    # by default DetailView returns 'book' context dict
    # changing that to 'book_detail'
    context_object_name = 'book_detail'
    model = models.Book
    template_name = 'cbvs/book_detail.html'

class BookCreateView(CreateView):
    model = models.Book
    fields = '__all__'

class BookUpdateView(UpdateView):
    model = models.Book
    fields = '__all__'

class BookDeleteView(DeleteView):
    model = models.Book
    success_url = reverse_lazy("cbvs:book_list")


