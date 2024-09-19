from django.shortcuts import render
from blog.models import Post
from  django.http import Http404

def post_list(request):
    posts=Post.publisheed.all()
    return render(request,'blog/post/list.html',{'posts': posts})

def post_detail(request,id):
     try:
            post=Post.publisheed.get(id=id)
     except Post.DoesNotExist:
          raise Http404("no Post found.")
     return render (request,'blog/post/list.html',{'post': post})
    

# Create your views here.
