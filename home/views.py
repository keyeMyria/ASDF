
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
#from home.forms import HomeForm,CommentForm
#from home.models import post,comment
from django.contrib.auth.models import User
#from django.views.generic import TemplateView
#from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post, Comment,Addlikes
from .forms import PostForm, CommentForm


def post_detail(request, pk):
    post = get_object_or_404(Post,pk=request.pk)
    return render(request, 'home/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.created = timezone.now()
            post.save()
            return redirect('/home/post')
    else:
        form = PostForm()
    return render(request, 'home/add.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('/home/post')
    else:
        form = PostForm(instance=post)
    return render(request, 'home/post_edit.html', {'form': form})


def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user == post.user:
        post.delete()
    return redirect('/home/post')

def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('/home/post')
    else:
        form = CommentForm()
    return render(request, 'home/comment.html', {'form': form})

def like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    likes = Addlikes.objects.all()
    print (post)
    print (likes.text)
    #print (likes.user_id)
    if request.method == "GET":
        p = Post.objects.get(pk=pk)
        p.likes+=1
        p.save()
        b = Addlikes(post=post, user=request.user)
        b.save()
    return HttpResponseRedirect('/home/post/'+pk)


#def search(request):
