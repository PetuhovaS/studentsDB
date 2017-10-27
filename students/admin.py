from django.contrib import admin



# Register your models here.
from students.models.students import Student

admin.site.register(Student)