from django.urls import path
from .views import PostListView
from . import views

urlpatterns = [
    path('community/', views.community, name='community'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/', views.post, name='post'),
    path('edit_post/<int:post_id>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]
