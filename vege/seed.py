from faker import Faker
import random
from .models import *
from django.db.models import Sum
fake = Faker()
def seed_sub_marks(n=121):
    try:
        student_objs = Student.objects.all()
        for student in student_objs:
            subject_objs = Subject.objects.all()
            for subject in subject_objs:
                SubjectMarks.objects.create(subject= subject, student= student,marks=random.randint(0, 100))
    except Exception as e:
        print(e)
def seed_db (n=100)->None:
    try:
        for i in range (0, n):
            department_objs = Department.objects.all()
            random_index = random.randint(0, len(department_objs)-1)
            student_id= f'STU--{random.randint(100, 999)}'
            department = department_objs[random_index]
            student_name= fake.name()
            student_email= fake.email()
            student_age= random.randint(18, 35)
            student_address= fake.address()
            student_id_obj =StudentID.objects.create(student_id=student_id)
            student_obj = Student.objects.create(
                student_id=student_id_obj,
                department=department,
                student_name=student_name,
                student_age= student_age,
                student_email= student_email,
                student_address= student_address)
            student_obj.save()
    except Exception as e:
        print(e)
def generate_report_card():
    i =1
    ranks = Student.objects.annotate(marks = Sum('studentmarks__marks')).order_by('-marks','-student_age')
    for rank in ranks:
        ReportCard.objects.create(student=rank, student_rank =i)
        i=i+1
