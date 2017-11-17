from django.contrib import admin

# Register your models here.
from instructor.models import Instructors, Spisok

admin.site.register(Instructors)
admin.site.register(Spisok)