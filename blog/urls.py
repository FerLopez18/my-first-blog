from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.post_list),
    path ('/post/<int:pk>/', views.post_detail, name='post_detail'),
]
