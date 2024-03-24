from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('community/', views.community, name='community'),
    path('', PostListView.as_view(), name='post_list'),
    path('post', views.post, name='post'),
]
