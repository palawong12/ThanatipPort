from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings
from django.template.loader import render_to_string

from .forms import PostForm, PostImgForm
from .filters import PostFilter, ImgFilter

from .models import Post, PostImg



def snakegame(request):
    return render(request, 'base/snakegame.html')

def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]

    context = {'posts': posts}
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

	context = {'post':post}
	return render(request, 'base/post.html', context)


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

def profile(request):
	return render(request, 'base/profile.html')


	#Thailand
def hometh(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]

    context = {'posts': posts}
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

	context = {'img':img}
	return render(request, 'base/postimg.html', context)


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


@login_required(login_url="home")
def deleteImg(request, slug):
	img = PostImg.objects.get(slug=slug)

	if request.method == 'POST':
		img.delete()
		return redirect('album')
	context = {'item':img}
	return render(request, 'base/deleteimg.html', context)