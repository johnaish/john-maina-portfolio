from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Project, Post
from .forms import ContactForm
from django.contrib import messages

def home(request):
    profile = Profile.objects.first()
    featured = Project.objects.filter(featured=True).order_by('-created_at')[:6]
    latest_posts = Post.objects.order_by('-published_at')[:3]
    return render(request, 'home.html', {'profile': profile, 'featured': featured, 'latest_posts': latest_posts})

def about(request):
    profile = Profile.objects.first()
    return render(request, 'about.html', {'profile': profile})

def portfolio(request):
    projects = Project.objects.exclude(image='')
    return render(request, 'portfolio.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def blog(request):
    posts = Post.objects.order_by('-published_at')
    return render(request, 'blog.html', {'posts': posts})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message sent — thank you!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
