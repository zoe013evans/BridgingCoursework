from django.contrib import admin
from .models import Post
from .models import Education
from .models import Project
from .models import Section
from .models import cvSection
# Register your models here.

admin.site.register(Post)

admin.site.register(Education)

admin.site.register(Project)

admin.site.register(Section)

admin.site.register(cvSection)


