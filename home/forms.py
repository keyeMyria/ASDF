from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'post',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)


'''from django import forms
from home.models import post,comment


class HomeForm(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
	attrs={
	'placeholder':'Enter your Blog post'
	}
	))
	type = forms.CharField(widget=forms.TextInput(
	attrs={
	'placeholder':'Enter the Type of Post'
	}
	))

	class Meta:
		model = post
		fields = ('post','type')

class CommentForm(forms.ModelForm):
	comment = forms.CharField(widget=forms.TextInput(
	attrs={
	'placeholder':'Enter your Comment'
	}
	))

	class Meta:
		model = comment
		fields = ('comment',)

'''
