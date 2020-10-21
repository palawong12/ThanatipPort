from django import forms
from django.forms import ModelForm

from .models import Post, PostTH

class PostForm(ModelForm):

	class Meta:
		model = Post
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}


class PostFormTH(ModelForm):

	class Meta:
		model = PostTH
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}