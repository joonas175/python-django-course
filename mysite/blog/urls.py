from django.urls import path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('', views.starting_page, name='starting-page'),
    path('posts/', views.all_posts, name='posts'),
    path('posts/<slug:slug>/', views.post, name='post-detail-page'),
]
