from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Receipe)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Subject)
class SubjectMarkAdmin(admin.ModelAdmin):
    # this will allow the display of each student with its subject and marks...
    list_display=['student', 'subject', 'marks']
admin.site.register(SubjectMarks, SubjectMarkAdmin)