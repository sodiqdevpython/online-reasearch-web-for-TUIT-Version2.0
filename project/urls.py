from django.urls import path
from .views import home_page, detail_article, UpdateArticle, create_project, add_group, groups_list, UpdateGroup, article_list, AdminUpdateArticle#, submit_task_form
urlpatterns = [
    path('', home_page, name='home'),
    path('mavzu/<str:slug>/', detail_article, name='detail'),
    path('mavzu/<str:slug>/tahrirlash/', UpdateArticle.as_view(), name="edit"),
    path('yangi-mavzu/', create_project, name='create'),
    path('yangi-gurux/', add_group, name="create_group"),
    path('guruxlar/', groups_list, name='groups'),
    path('guruxlar/<int:pk>/', UpdateGroup.as_view(), name="group_detail"),
    path('mavzular-royxati/', article_list, name='article_list'),
    path('mavzu/<str:slug>/tahrirlash/admin', AdminUpdateArticle.as_view(), name="edit_article_admin"),
    # path('mavzu/<str:slug>/sign_up', submit_task_form, name='submit_task')
]