from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'create.html')
def update(request):
    return render(request, 'update.html')
def select(request):
    return render(request, 'select.html')
def delete(request):
    return render(request, 'delete.html')