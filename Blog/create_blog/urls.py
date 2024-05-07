from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('create-blog/', views.create_blog),
    path('blogs-list/', views.blogs_list, name='blogs_list'),
    path('<int:pk>/', views.blog_detail, name='blog_detail'),
    path('<int:pk>/update/', views.blog_update, name='blog_update'),
    path('blogs/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('', include('posts.urls')),
]
