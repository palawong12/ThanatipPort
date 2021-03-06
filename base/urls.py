from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('posts/', views.posts, name="posts"),
	path('post/<slug:slug>/', views.post, name="post"),
	path('post/snake/snakegame/', views.snakegame, name='snakegame'),

	#Login
	path('login/', views.loginPage, name="login"),
	path('register/', views.registerPage, name="register"),
	path('logout/', views.logoutUser, name="logout"),
	path('account/', views.userAccount, name="account"),
	path('update_profile/', views.updateProfile, name="update_profile"),

	#Images Post
	path('album/', views.imgs, name="album"),
	path('postimg/<slug:slug>/', views.img, name="img"),
	path('create_postimg/', views.createImg, name="create_img"),
	path('update_img/<slug:slug>/', views.updateImg, name="update_img"),
	path('delete_img/<slug:slug>/', views.deleteImg, name="delete_img"),


	#UPDATE PATHS
	path('create_post/', views.createPost, name="create_post"),
	path('update_post/<slug:slug>/', views.updatePost, name="update_post"),
	path('delete_post/<slug:slug>/', views.deletePost, name="delete_post"),
	path('send_email/', views.sendEmail, name="send_email"),



	#Thailand
	path('hometh/', views.hometh, name="hometh"),
	path('mainth/', views.mainth, name='mainth'),
	path('navbarth/', views.navbarth, name="navbarth"),
	#path('poststh/', views.poststh, name="poststh"),
	#path('postth/<slug:slug>/', views.postth, name="postth"),
	#path('create_postth/', views.createPostTH, name="create_postth"),
	#path('update_postth/<slug:slug>/', views.updatePostTH, name="update_postth"),
	#path('delete_postth/<slug:slug>/', views.deletePostTH, name="delete_postth"),
]