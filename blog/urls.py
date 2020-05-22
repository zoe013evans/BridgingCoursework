from django.urls import path 
from . import views 



urlpatterns = [

	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name = 'post_detail'),
	path('post/new/', views.post_new, name='post_new'), 
	path('post/<int:pk>/edit/', views.post_edit, name="post_edit")
]

#post/ means the URL should begin with word post followed by a / 
#<int:pk> means an int is expected. This variable is called pk. 
#/ then we do a slash to finish the url lol