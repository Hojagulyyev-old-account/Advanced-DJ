from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('another/', views.AnotherView.as_view(), name='another'),
    path('genic/<int:range>/<str:method>/', views.generator),
]
