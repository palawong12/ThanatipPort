from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('posts/', views.posts, name="posts"),
	path('post/<str:pk>/', views.post, name="post"),
	path('profile/', views.profile, name="profile"),
	path('present/', views.present, name="present"),
	path('snake/', views.snake, name='snake'),
	#UPDATE PATHS

]