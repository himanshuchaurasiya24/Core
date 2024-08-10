# Generated by Django 3.2.25 on 2024-08-10 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0009_auto_20240806_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='RepostCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_report_card_generation', models.DateField(auto_created=True)),
                ('student_rank', models.IntegerField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentreportcard', to='vege.student')),
            ],
        ),
    ]
