from django.shortcuts import render
from django.http import HttpResponse
from blog.views import my_blog

# Create your views here.
def my_blog(request):
    return HttpResponse("Hello, Blog!")
