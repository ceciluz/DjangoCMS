from django.urls import path
from . import views
from django.conf.urls.static import static, serve
from django.conf import settings

app_name = 'users'

urlpatterns = [
     path('register/', views.register, name ='register'),
     path('login/', views.user_login, name='login'),
     path('profile/', views.profile, name='profile'),
     path('logout/', views.user_logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)