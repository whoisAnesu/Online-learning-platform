from django.contrib import admin

from .models import Book, Assignment, Video, Course, Submit, RegProfile, Registration

admin.site.register(Book)
admin.site.register(Assignment)
admin.site.register(Video)
admin.site.register(Course)
admin.site.register(Submit)
admin.site.register(RegProfile)
admin.site.register(Registration)
