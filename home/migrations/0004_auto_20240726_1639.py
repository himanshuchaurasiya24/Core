# Generated by Django 3.2.25 on 2024-07-26 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
