from django.urls import path
from . import views
from users import views as user_views  # Ye line comment karein agar error de

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
    # Simple register view directly include karein
    path('register/', views.user_register, name='register'),
]
