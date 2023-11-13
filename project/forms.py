from django import forms
from .models import Project, GroupName#, Attempt

# class ArticleUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Project

#         fields = [
#             "body"
#         ]

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        # fields = ['title', 'author', 'start_time', 'end_time', 'type','slug', 'image', 'body']
        fields = "__all__"

class CreateGroup(forms.ModelForm):
    class Meta:
        model = GroupName
        fields = "__all__"

# class RegisterAtricle(forms.ModelForm):
#     class Meta:
#         model = Attempt
#         fields = "__all__"