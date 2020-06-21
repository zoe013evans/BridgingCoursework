from django import forms 

from .models import Post 
from .models import Project
from .models import Education

class PostForm(forms.ModelForm):

	class Meta: 
		model = Post
		fields = ('title', 'text',)








##PostForm = name of forms 
#It's a model form, apparently. 

#Meta is for telling Django which model should
#be used to create the form. Obvi Post. 

class ProjectForm(forms.ModelForm):

	class Meta: 
		model = Project
		fields = ('text',)



