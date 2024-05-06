from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # fields = ['title', 'author', 'start_time', 'end_time', 'type','slug', 'image', 'body']
        fields = "__all__"