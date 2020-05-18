from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.


def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')



	#We're trying to connect mdodels and templates
	#In a view we deicde what model will be displayed
	#in a template



	return render(request, 'blog/post_list.html', {'posts':posts})

	#Creating a function (def) called post_list. 
	#It takes a request and returns the value it gets from calling
	#Another function render. 

	#Render puts together the template. 

