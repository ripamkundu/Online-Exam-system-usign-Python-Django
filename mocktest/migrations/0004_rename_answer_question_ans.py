# Generated by Django 3.2.6 on 2021-12-19 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mocktest', '0003_question_answer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='answer',
            new_name='ans',
        ),
    ]