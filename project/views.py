from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from .models import Project

from .forms import ProjectForm


def home_page(request):
    if request.user.is_authenticated:
        data = Project.objects.all()

        count_data = data.count()
        context = {
            'data': data,
            'count_data': count_data
        }
        return render(request, 'index.html', context)
    else:
        return render(request, 'login.html')


from django.shortcuts import render, get_object_or_404
from .models import Project
from django.utils import timezone


def detail_article(request, slug):
    data_base = get_object_or_404(Project, slug=slug)
    current_time = timezone.now()

    if data_base.start_time <= current_time.date() <= data_base.end_time and data_base.who_can_edit == request.user:
        editable = True
    else:
        editable = False

    context = {
        'data_base': data_base,
        'editable': editable
    }
    return render(request, 'detail.html', context)


class UpdateArticle(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'edit_article.html'
    fields = ('body',)
    slug_field = 'slug'
    success_url = '/'


def create_project(request):
    project_count = Project.objects.all().filter(author=request.user).count()
    if request.user.article_num.arcticle_number > project_count:
        is_allowed = True
    else:
        is_allowed = False
    print(is_allowed)
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            return redirect('/', slug=project.slug)
    else:
        form = ProjectForm()
    return render(request, 'create_article.html',
                  {'form': form, 'project_count': project_count, 'is_allowed': is_allowed})


def article_list(request):
    article = Project.objects.all().filter(author=request.user)
    context = {
        'article': article
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


def user_profile(request, username):
    user = get_object_or_404(User, username=username)

    context = {
        'user': user
    }

    return render(request, 'user_profile.html', context)