from django.shortcuts import render,redirect
from . models import Post
from django.http import JsonResponse
from . forms import PostForm

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request,'blog/index.html',context)

def post_detail(request,pk):
    post = Post.objects.get(id=pk)
    context = {
        'post':post,
    }
    return render(request,'blog/detail.html',context)

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    context = {
        'form':form,
    }
    return render(request,'blog/create.html',context)

def post_update(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostForm(instance=post,data = request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request,'blog/create.html',context)

def post_delete(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    context = {
        'post':post
    }
    return render(request,'blog/confirm.html',context)