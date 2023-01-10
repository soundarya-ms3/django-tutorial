from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello worl")

def products(request):
    
    return HttpResponse("<h1>List of products</h1>") 