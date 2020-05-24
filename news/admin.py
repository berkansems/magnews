from django.contrib import admin

# Register your models here.
from news.models import News

admin.site.register(News)
