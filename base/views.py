from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string
from .forms import PostForm, PostImgForm, CustomUserCreationForm, ProfileForm, UserForm
from .filters import PostFilter, ImgFilter
from django.contrib.auth import logout, login, authenticate
from .decorators import *	
from .models import *


def game(request):
    return render(request, 'base/game.html')

def snakegame(request):
    return render(request, 'base/snakegame.html')

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    imgs = PostImg.objects.filter(active=True, featured=True)[0:3]
    context = {'posts': posts, 'imgs': imgs}
    return render(request, 'base/index.html', context)


def posts(request):
	posts = Post.objects.filter(active=True)
	myFilter = PostFilter(request.GET, queryset=posts)
	posts = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(posts, 5)

	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	context = {'posts':posts, 'myFilter':myFilter}
	return render(request, 'base/posts.html', context)


def post(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		PostComment.objects.create(
			author=request.user.profile,
			post=post,
			body=request.POST['comment']
			)
		messages.success(request, "You're comment was successfuly posted!")

		return redirect('post', slug=post.slug)


	context = {'post':post}
	return render(request, 'base/post.html', context)


@admin_only
@login_required(login_url="home")
def createPost(request):
	form = PostForm()

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'base/post_form.html', context)


@admin_only
@login_required(login_url="home")
def updatePost(request, slug):
	post = Post.objects.get(slug=slug)
	form = PostForm(instance=post)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance=post)
		if form.is_valid():
			form.save()
		return redirect('posts')

	context = {'form':form}
	return render(request, 'base/post_form.html', context)

@admin_only
@login_required(login_url="home")
def deletePost(request, slug):
	post = Post.objects.get(slug=slug)

	if request.method == 'POST':
		post.delete()
		return redirect('posts')
	context = {'item':post}
	return render(request, 'base/delete.html', context)




def sendEmail(request):

	if request.method == 'POST':

		template = render_to_string('base/email_template.html', {
			'name':request.POST['name'],
			'email':request.POST['email'],
			'message':request.POST['message'],
			})

		email = EmailMessage(
			request.POST['subject'],
			template,
			settings.EMAIL_HOST_USER,
			['jakkapan225@gmail.com']
			)

		email.fail_silently=False
		email.send()

	return render(request, 'base/email_sent.html')

#New 
def loginPage(request):

	if request.method == 'POST':
		email = request.POST.get('email')
		password =request.POST.get('password')

		#Little Hack to work around re-building the usermodel
		try:
			user = User.objects.get(email=email)
			user = authenticate(request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('login')
			
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Email OR password is incorrect')

	context = {}
	return render(request, 'base/login.html', context)

def registerPage(request):
	form = CustomUserCreationForm()
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			messages.success(request, 'Account successfuly created!')

			user = authenticate(request, username=user.username, password=request.POST['password1'])

			if user is not None:
				login(request, user)

			next_url = request.GET.get('next')
			if next_url == '' or next_url == None:
				next_url = 'home'
			return redirect(next_url)
		else:
			messages.error(request, 'An error has occured with registration')
	context = {'form':form}
	return render(request, 'base/register.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')

@login_required(login_url="home")
def userAccount(request):
	profile = request.user.profile

	context = {'profile':profile}
	return render(request, 'base/account.html', context)

@login_required(login_url="home")
def updateProfile(request):
	user = request.user
	profile = user.profile
	form = ProfileForm(instance=profile)
	if request.method == 'POST':
		user_form = UserForm(request.POST, instance=user)
		if user_form.is_valid():
			user_form.save()

		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			form.save()
			return redirect('account')


	context = {'form':form}
	return render(request, 'base/profile_form.html', context)





	#Thailand
def hometh(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    imgs = PostImg.objects.filter(active=True, featured=True)[0:3]
    context = {'posts': posts, 'imgs': imgs}
    return render(request, 'base/indexth.html', context)


def navbarth(request):
    return render(request, 'base/navbarth.html')

def mainth(request):
    return render(request, 'base/mainth.html')


#########################################################################################
def imgs(request):
	imgs = PostImg.objects.filter(active=True)
	myFilter = ImgFilter(request.GET, queryset=imgs)
	imgs = myFilter.qs

	page = request.GET.get('page')

	paginator = Paginator(imgs, 6)

	try:
		imgs = paginator.page(page)
	except PageNotAnInteger:
		imgs = paginator.page(1)
	except EmptyPage:
		imgs = paginator.page(paginator.num_pages)

	context = {'imgs':imgs, 'myFilter':myFilter}
	return render(request, 'base/gallerylist.html', context)


def img(request, slug):
	img = PostImg.objects.get(slug=slug)
	if request.method == 'POST':
		ImgComment.objects.create(
			author=request.user.profile,
			post=img,
			body=request.POST['comment']
			)
		messages.success(request, "You're comment was successfuly posted!")

		return redirect('img', slug=img.slug)
	context = {'img':img}
	return render(request, 'base/postimg.html', context)

@admin_only
@login_required(login_url="home")
def createImg(request):
	form = PostImgForm()

	if request.method == 'POST':
		form = PostImgForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('album')

	context = {'form':form}
	return render(request, 'base/postimg_form.html', context)


@admin_only
@login_required(login_url="home")
def updateImg(request, slug):
	img = PostImg.objects.get(slug=slug)
	form = PostImgForm(instance=img)

	if request.method == 'POST':
		form = PostImgForm(request.POST, request.FILES, instance=img)
		if form.is_valid():
			form.save()
		return redirect('album')

	context = {'form':form}
	return render(request, 'base/postimg_form.html', context)

@admin_only
@login_required(login_url="home")
def deleteImg(request, slug):
	img = PostImg.objects.get(slug=slug)

	if request.method == 'POST':
		img.delete()
		return redirect('album')
	context = {'item':img}
	return render(request, 'base/deleteimg.html', context)