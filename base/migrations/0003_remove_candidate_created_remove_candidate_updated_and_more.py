# Generated by Django 4.1.7 on 2023-02-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_user_delete_admin_delete_student_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='created',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='updated',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='rank',
            field=models.CharField(max_length=10, null=True),
        ),
    ]