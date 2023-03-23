from django.urls import path,include
from user import views

urlpatterns = [
  path('', views.home, name='home'),
  path('login/', views.login_user, name='login'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register_user, name='register'),
  path('new_task/', views.new_task, name='new_task'),
  path('view_uncompleted/', views.view_uncompleted, name='view_uncompleted'),
  path('update_task/<int:pk>/', views.update_task, name='update_task'),
  path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
