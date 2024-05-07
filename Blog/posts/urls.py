from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
     path('<int:id_blog>/post/<int:id_post>/', views.post_detail, name='post_detail'),
     path('<int:id_blog>/post/<int:id_post>/update/', views.post_update, name='post_update'),
     path('<int:id_blog>/post/<int:id_post>/edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment'),
     path('<int:id_blog>/create-post/', views.create_post, name ='create_post'),
]
