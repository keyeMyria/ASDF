from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=500,default="TITLE")
	post = models.TextField(max_length=500,default="POST")
	user =  models.ForeignKey(User,on_delete=models.CASCADE, )
	created = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default = 0)

	def __str__(self):
		return self.title

class Comment(models.Model):
    post = models.ForeignKey('home.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, default='xxxxx')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

class Addlikes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='xxxxx')
    liketime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post
