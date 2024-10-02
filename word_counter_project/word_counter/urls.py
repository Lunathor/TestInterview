from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload-file/', views.upload_file, name='upload_file'),
    path('word-count/', views.word_count, name='word_count'),
    path('clear-data/', views.clear_data, name='clear_data'),
]