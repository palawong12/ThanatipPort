from django import forms
from django.forms import ModelForm

from .models import Post, Tag

class PostForm(ModelForm):

	class Meta:
		model = Post
		fields = '__all__'