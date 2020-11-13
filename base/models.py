from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User


class Tag(models.Model):
	name = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Post(models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, null=True, blank=True)
	picture = models.ImageField(null=True, blank=True, upload_to="images", default="placeholder.png")
	body = RichTextUploadingField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)
	
	def __str__(self):
		return self.headline

	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.headline)

			has_slug = Post.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.headline) + '-' + str(count) 
				has_slug = Post.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)

class PostImg(models.Model):
	headline = models.CharField(max_length=200)
	sub_headline = models.CharField(max_length=200, null=True, blank=True)
	picture = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	body = RichTextUploadingField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)
	picture1 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	picture2 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	picture3 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	picture4 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	picture5 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	picture6 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	picture7 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	picture8 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	picture9 = models.ImageField(null=True, blank=True, upload_to="gallerys", default="placeholder.png")
	active = models.BooleanField(default=False)
	featured = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	slug = models.SlugField(null=True, blank=True)
	
	def __str__(self):
		return self.headline
		
	def save(self, *args, **kwargs):

		if self.slug == None:
			slug = slugify(self.headline)

			has_slug = PostImg.objects.filter(slug=slug).exists()
			count = 1
			while has_slug:
				count += 1
				slug = slugify(self.headline) + '-' + str(count) 
				has_slug = PostImg.objects.filter(slug=slug).exists()

			self.slug = slug

		super().save(*args, **kwargs)



class Profile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=200, blank=True, null=True)
	last_name = models.CharField(max_length=200, blank=True, null=True)
	email = models.CharField(max_length=200)
	profile_pic = models.ImageField(null=True, blank=True, upload_to="images", default="/user.png")
	bio = models.TextField(null=True, blank=True)
	#twitter = models.CharField(max_length=200,null=True, blank=True)

	def __str__(self):
		name = str(self.first_name)
		if self.last_name:
			name += ' ' + str(self.last_name)
		return name

class PostComment(models.Model):
	author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.body

	@property
	def created_dynamic(self):
		now = timezone.now()
		return now

class ImgComment(models.Model):
	author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
	body = models.TextField(null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return self.body

	@property
	def created_dynamic(self):
		now = timezone.now()
		return now