# Generated by Django 4.2.6 on 2023-10-17 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_quiz_previous_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='previous_question',
        ),
    ]