from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.all()
    #SELECT * FROM posts_post
    return render(request,'posts/index.html',{'posts':posts})

# def index2(request):
#     post = Post.objects.filter(location='汐止地區')
#     #SELECT * FROM posts_post WHERE location="汐止地區"
#     return HttpResponse(post)