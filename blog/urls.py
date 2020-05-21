from django.urls import path 
from . import views 



urlpatterns = [

	path('', views.post_list, name='post_list'),
	path('post/<int:pk>/', views.post_detail, name = 'post_detail'),

]

#post/ means the URL should begin with word post followed by a / 
#<int:pk> means an int is expected. This variable is called pk. 
#/ then we do a slash to finish the url lol