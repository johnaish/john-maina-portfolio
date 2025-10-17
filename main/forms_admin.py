from django import forms
from .models import Project, Post

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title','description','image','category','featured']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image']
