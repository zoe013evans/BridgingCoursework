from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Project
from django.utils import timezone
from .forms import PostForm
from .forms import ProjectForm
from .models import Education
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from itertools import chain 
from .models import Section
from .models import cvSection
# Create your views here.



def main_page(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/mainpage.html', {'posts':posts})

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

@login_required

def post_new(request):
	if request.method == "POST":
			form = PostForm(request.POST)
			if form.is_valid():
				post = form.save(commit = False)
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				return redirect('post_detail', pk = post.pk)
	else:	
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else: 
		form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_publish(request, pk):
	post = get_object_or_404(Post, pk=pk)
	post.publish()
	return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk): 
	post = get_object_or_404(Post, pk=pk)
	post.delete()
	return redirect('post_list.html')


def cv(request):
	education = Education.objects.filter(end_date__lte=timezone.now()).order_by('end_date')
	project = Project.objects.filter(date__lte=timezone.now()).order_by('date')
	section = cvSection.objects.filter(date_end__lte=timezone.now())
	return render(request, 'blog/cv.html', {'section':section})

def project_detail(request, pk): 
	project = get_object_or_404(Projects, pk = pk)
	return render(request, 'blog/project_detail.html', {'project': projects})		
	








def projects_new(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.date = timezone.now()
			project.save()
			return redirect('cv')
	else: 
		form = ProjectForm