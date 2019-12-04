from django.shortcuts import render
from django.views.generic import (View,
                                  TemplateView,
                                  CreateView,
                                  ListView,
                                  UpdateView,
                                  DeleteView)
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from . import models

# Create your views here.

"""
def index(request):
    return HttpResponse("This is from Class based Views")
"""

class CBVSViw(View):
    def get(self, request):
        return HttpResponse("<h1>This is from Class based Views</h1>")


class CBVSTemplateView(TemplateView):
    template_name = 'cbvs/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['add_item'] = 'Select Books or Libraries'
        return context

class LibraryListView(ListView):
    # by default ListView returns library_list context dict.
    # changing that to 'libraries'
    context_object_name = 'libraries'
    model = models.Library

class LibraryDetailView(DeleteView):
    # by default DetailView returns 'library' context dict
    # changing that to 'library_detail'
    context_object_name = 'library_detail'
    model = models.Library
    template_name = 'cbvs/library_detail.html'

class LibraryCreateView(CreateView):
    model = models.Library
    fields = ('name', 'books', 'location')

class LibraryUpdateView(UpdateView):
    model = models.Library
    fields = ('name','books')

class LibraryDeleteView(DeleteView):
    model = models.Library
    success_url = reverse_lazy("cbvs:list")


