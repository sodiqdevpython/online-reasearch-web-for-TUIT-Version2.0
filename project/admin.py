from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Project,TeacherArticleCreateNumber, GroupName#,Attempt
# Register your models here.

@admin.register(Project)
class AdminViewProject(admin.ModelAdmin):
    list_display = ['title','author','created_time']
    date_hierarchy = 'created_time'
    prepopulated_fields = {"slug": ('title',)}
    search_fields = ['title','body']

# admin.site.register(Chose)
admin.site.register(GroupName)

UserAdmin.search_fields = ('username', 'email')

class TeacherArticleNum(admin.ModelAdmin):
    autocomplete_fields = ['user']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(TeacherArticleCreateNumber, TeacherArticleNum)

# admin.site.register(Attempt)