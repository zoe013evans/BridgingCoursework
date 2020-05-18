from django.shortcuts import render

# Create your views here.


def post_list(request):
	return render(request, 'blog/post_list.html', {})

	#Creating a function (def) called post_list. 
	#It takes a request and returns the value it gets from calling
	#Another function render. 

	#Render puts together the template. 