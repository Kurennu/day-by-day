from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('manager/<int:user_id>/', views.manager_home, name='manager_home'),
]
