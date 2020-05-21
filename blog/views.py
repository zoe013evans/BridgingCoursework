from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from .forms import PostForm

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

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

