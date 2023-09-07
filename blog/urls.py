from django.urls import path
from . import views

urlpatterns = [
   path('bloglist/', views.post_list, name='post_list'),
   path('post_detail/<int:post_id>/', views.post_detail, name='post_detail'),


]
