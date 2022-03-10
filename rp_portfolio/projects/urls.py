from django.contrib import admin
from django.urls import path, include
from projects import views

urlpatterns = [
    path('', views.main_index, name='main_index'),
    path('projects/', views.project_index, name='project_index'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),    
    path('blog/', include('blog.urls')),    
    path('users/', include('users.urls')),
]