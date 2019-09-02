from django.contrib import admin
from quotes.models import Author, Quote

# Register your models here.
admin.site.register([Author, Quote])
