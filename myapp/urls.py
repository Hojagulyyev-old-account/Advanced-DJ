from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.HomeIndexView.as_view(), name='home'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('another/', views.AnotherView.as_view(), name='another'),
]
