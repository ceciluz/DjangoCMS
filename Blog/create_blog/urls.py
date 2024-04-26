from django.urls import path
from . import views

urlpatterns = [
    path('create-blog/', views.create_blog),
    path('blogs-list/', views.blogs_list, name='blogs_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/update/', views.blog_update, name='blog_update'),
]
