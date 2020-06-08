from django.contrib import admin

# Register your models here.
from contactform.models import ContactForm, Comments

admin.site.register(ContactForm)

admin.site.register(Comments)