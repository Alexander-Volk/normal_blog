from django.urls import path
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', post_list, name='post_list_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url')
]