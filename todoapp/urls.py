from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.homepage, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/verify/', views.login, name='verify'),
    path('dashboard/add/', views.addTaskPage, name='addTaskPage'),
    path('dashboard/add/verify/', views.addTask, name='addTask'),
    path('dashboard/update/<int:id>', views.updateTask, name='updateTask'),
    path('dashboard/delete/<int:id>', views.deleteTask, name='deleteTask'),
    path('dashboard/logout/', views.logout, name='logout'),
]