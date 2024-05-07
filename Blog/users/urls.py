from django.urls import path
from . import views
from django.conf.urls.static import static, serve
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

app_name = 'users'

urlpatterns = [
     path('register/', views.register, name ='register'),
     path('accounts/login/', LoginView.as_view(), name='login'),
     path('accounts/profile/', views.profile, name='profile'),
     path('accounts/logout/', views.user_logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

