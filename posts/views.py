from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post
import requests

# Create your views here.
def index(request):
    #posts = Post.objects.all()
    #SELECT * FROM posts_post
    #return render(request,'posts/index.html',{'posts':posts})

    response = requests.get('https://emma.pixnet.cc/mainpage/blog/categories/hot/28')
    articles = response.json()['articles']
    return render(request,'posts/index.html',{'articles':articles})