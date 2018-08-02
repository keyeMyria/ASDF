from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	desc = models.CharField(max_length=100,default='')
	city = models.CharField(max_length=20,default='')
	phone = models.IntegerField(default=0)
	pinc = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username

"""
clas
s BlogPost(models.Model):
	title = models.CharField(default="NO TITLE")
	description = models.TextField(default="NO Description")
	User = models.TextField(default="NO TITLE")
"""
