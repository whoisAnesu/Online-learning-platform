from django.contrib import admin
from .models import Category, News, Comments

admin.site.register(Category)
admin.site.register(News)
admin.site.register(Comments)
