from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy #, UserPassesTestMixin
from django.views.generic import UpdateView#, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from .models import Project,GroupName#, Attempt

from .forms import ProjectForm, CreateGroup #,RegisterAtricle

# Create your views here.
# @login_required
def home_page(request):
    if request.user.is_authenticated:
        #.filter(followers = request.user).order_by('id')
        # data = Chose.objects.all().filter(students_list = request.user).order_by('id')
        data_group = GroupName.objects.all().filter(student_list=request.user)
        data = Project.objects.all()
        
        count_data = data.count()
        context = {
            'data': data,
            'count_data':count_data,
            'data_group':data_group
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'login.html')
    # if Chose.objects.filter(students=request.user):
    #     return render(request, 'home_page.html', context)
    # else:
    #     return HttpResponse("Forbidden")

def detail_article(request, slug):
    data_base = get_object_or_404(Project, slug=slug)
    context = {
        'data_base': data_base
    }
    return render(request, 'detail.html', context)

class UpdateArticle(LoginRequiredMixin, UpdateView):

    model = Project
    template_name = 'edit_article.html'
    fields = ('body',)
    slug_field = 'slug'
    success_url = '/'



    # def test_func(self):
    #     obj = self.get_object()

    #     return obj.followers.filter(id=self.request.user.id).exists()

# class CreateArticle(CreateView):
#     model = Project
#     template_name = 'create_article.html'
#     success_url = '/'
#     # success_url = reverse_lazy('home.html')
#     fields = '__all__'
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['all_users'] = User.objects.all()
#         return context

def add_group(request):
    form = CreateGroup(request.POST or None)
    if form.is_valid() and request.method=="POST":
        form.save()
        redirect("home")
        return redirect('groups')
    context = {
        'form': form
    }
    return render(request, 'create_group.html', context)

# def create_article(request):
#     form = ArticleCreateForm(request.POST or None)
#     all_users = User.objects.all()
#     if form.is_valid() and request.method=="POST":
#         form.save()
#         return HttpResponse("<h2>Yangi mavzu yaratildi !</h2>")
#     context = {
#         'form': form,
#         'all_users':all_users
#     }
#     return render(request, 'create_article.html', context)

def create_project(request):
    project_count = Project.objects.all().filter(author=request.user).count()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('/', slug=project.slug)
    else:
        form = ProjectForm()
    return render(request, 'create_article.html', {'form': form,'project_count':project_count})

def groups_list(request):
    group_list = GroupName.objects.all()
    context = {
        'group_list':group_list
    }
    return render(request, 'groups.html', context)

class UpdateGroup(UpdateView):
    model = GroupName
    template_name = 'edit_group.html'
    fields = '__all__'
    success_url = '/'


def article_list(request):
    article = Project.objects.all().filter(author = request.user)
    context = {
        'article':article
    }
    return render(request, 'article_list.html', context)

class AdminUpdateArticle(UpdateView):
    model = Project
    template_name = 'admin_edit_article.html'
    fields = '__all__'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# def submit_task_form(request, slug):                
#     data = get_object_or_404(Project, slug=slug)
    
#     if request.method == "POST":
#         form = RegisterAtricle(request.POST)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.user = request.user
#             form.save()
#             return redirect('home')
#     else:
#         form = RegisterAtricle(instance=data)

#     context = {
#         'data': data,
#         'form': form,
#     }
#     return render(request, 'agree_edit_article.html', context)