from django.contrib import admin

#adding models here will display pages in the admin page.
from .models import Question

admin.site.register(Question)