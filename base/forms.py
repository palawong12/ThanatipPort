from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, PostImg, Profile

class PostForm(ModelForm):

	class Meta:
		model = Post
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}

class PostImgForm(ModelForm):

	class Meta:
		model = PostImg
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}
class CustomUserCreationForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email']
		

class ProfileForm(ModelForm):
	class Meta:
		model = Profile
		fields = '__all__'
		exclude = ['user']