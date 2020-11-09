from django import forms
from django.forms import ModelForm

from .models import Post, PostImg

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
