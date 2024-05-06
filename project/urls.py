from django.urls import path
from .views import home_page, detail_article, UpdateArticle, create_project, article_list, AdminUpdateArticle, user_profile
urlpatterns = [
    path('', home_page, name='home'),
    path('mavzu/<str:slug>/', detail_article, name='detail'),
    path('mavzu/<str:slug>/tahrirlash/', UpdateArticle.as_view(), name="edit"),
    path('yangi-mavzu/', create_project, name='create'),
    path('mavzular-royxati/', article_list, name='article_list'),
    path('mavzu/<str:slug>/tahrirlash/admin', AdminUpdateArticle.as_view(), name="edit_article_admin"),
    path('<str:username>/', user_profile, name='user_profile'),
]