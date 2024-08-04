from django.contrib import admin
from . import models

# Register your models here.
'''
Once your models are defined, Django can automatically create a professional, 
production ready administrative interface – a website that lets authenticated users
add, change and delete objects. The only step required is to register your
model in the admin site
'''
admin.site.register(models.Article)
admin.site.register(models.Reporter)
