from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    # path('<str:action>/home/manager', views.home_manager, name='home-manager'),

]
