from django.urls import path
from . import views

urlpatterns = [
    # url pattern value, view to use, and name
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
