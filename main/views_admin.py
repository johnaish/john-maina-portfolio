from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms_admin import ProjectForm, PostForm
from .models import Project, Post

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'admin_login.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def dashboard(request):
    projects = Project.objects.order_by('-created_at')
    posts = Post.objects.order_by('-published_at')
    return render(request, 'dashboard.html', {'projects':projects,'posts':posts})

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project created')
            return redirect('dashboard')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post created')
            return redirect('dashboard')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

from django.shortcuts import HttpResponse

@login_required
def edit_project(request, pk):
    proj = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=proj)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated')
            return redirect('dashboard')
    else:
        form = ProjectForm(instance=proj)
    return render(request, 'edit_project.html', {'form': form, 'project': proj})

@login_required
def delete_project(request, pk):
    proj = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        proj.image.delete(save=False)
        proj.delete()
        messages.success(request, 'Project deleted')
        return redirect('dashboard')
    return render(request, 'delete_project.html', {'project': proj})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated')
            return redirect('dashboard')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        if post.image:
            post.image.delete(save=False)
        post.delete()
        messages.success(request, 'Post deleted')
        return redirect('dashboard')
    return render(request, 'delete_post.html', {'post': post})
