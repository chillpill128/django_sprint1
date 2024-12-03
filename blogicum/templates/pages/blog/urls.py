
from django.urls import path
from .import views

app_name="blog"
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:inf>/', views.post_detail, name='post_detail'),
    path('category/<slug:inf>/', views.category_posts, name='category_posts'),

]