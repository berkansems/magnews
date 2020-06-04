from django.contrib import admin

# Register your models here.
from book.models import Book
from main.models import Main
from news.models import News

admin.site.register(Main)

admin.site.register(Book)
