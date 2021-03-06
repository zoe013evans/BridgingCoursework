from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here




class Post(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank=True, null = True)


	def publish(self): 
		self.published_date = timezone.now()
		self.save()


	def __str__(self): 
		return self.title 

		


class Education(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	text = models.TextField()
	

	def publish(self):
		self.save()

	



class Project(models.Model): 
	date = models.DateTimeField()
	text = models.TextField()


class Section(models.Model):
	date_start = models.DateField()
	date_end = models.DateField()
	title = models.CharField(max_length=200)
	text = models.TextField()
	
class cvSection(models.Model):
	date_start = models.DateField()
	date_end = models.DateField()
	title = models.CharField(max_length=200)
	detail = models.TextField()
	section_type = models.TextField()