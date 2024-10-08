from django.contrib import admin

# Register your models here.
from .models import *
from django.db.models import Sum
admin.site.register(Receipe)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentID)
admin.site.register(Subject)
class SubjectMarkAdmin(admin.ModelAdmin):
    # this will allow the display of each student with its subject and marks...
    list_display=['student', 'subject', 'marks']
admin.site.register(SubjectMarks, SubjectMarkAdmin)
class ReportCardAdmin(admin.ModelAdmin):
    def total_marks (self, obj):
        subject_marks = SubjectMarks.objects.filter(student = obj.student)
        return subject_marks.aggregate(marks = Sum('marks'))['marks']
    ordering = ['student_rank']
    list_display=['student', 'student_rank','total_marks', 'date_of_report_card_generation']
admin.site.register(ReportCard, ReportCardAdmin)
