from django.shortcuts import render
#from . import forms
from myform.forms import NewUserForm
# Create your views here.

def index (request):
    return render(request, 'myform/index.html')

def signup(request):
    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Invalid Form")

    return render(request, 'myform/signup.html', {'form':form})

def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Valdated!!!")
            print("Name :", form.cleaned_data['name'])
            print("EMail :", form.cleaned_data['email'])
            print("Remarks :", form.cleaned_data['text'])


    return render(request, 'myform/form_page.html', {'form':form})