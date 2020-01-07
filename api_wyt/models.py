from django.db import models

# Create your models here.

class thoughts(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200, blank=False,default='<No Title :3>')
	author = models.CharField(max_length=200,blank=False,default='<No Author :3>')
	description = models.CharField(max_length=500, blank=True,default='')
	
	class Meta:
		ordering = ('created',)
