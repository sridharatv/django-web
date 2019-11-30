from django.shortcuts import render
from django.http import HttpResponse

from myapp1.models import Publisher, Author, Book
# Create your views here.

def index(request):
    book_list = Book.objects.order_by('publication_date')
    bk_dict = {'books_published': book_list}

    #myd1 = {'from_tmp' : "getting data from templates"}
    return render(request, 'myapp1/index.html', context=bk_dict)

def image(request):
    myd1 = {'get_image' : "Loading image from static files"}
    return render(request, 'myapp1/image.html', context=myd1)

def awsrds(request):
    myd1 = {'get_video' : "AWS Relational Databases Intro"}
    return render(request, 'myapp1/awsrds.html', context=myd1)

def index2(request):
    return HttpResponse("<em>This is from my first app</em>")

def index1(request):
    return HttpResponse("<html><h1>This is from my first app</html></h1>")
