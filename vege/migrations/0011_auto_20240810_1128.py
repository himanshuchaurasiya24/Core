# Generated by Django 3.2.25 on 2024-08-10 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0010_repostcard'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RepostCard',
            new_name='ReportCard',
        ),
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'date_of_report_card_generation')},
        ),
    ]
