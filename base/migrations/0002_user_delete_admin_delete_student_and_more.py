# Generated by Django 4.1.7 on 2023-02-21 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('faculty', models.CharField(max_length=255, null=True)),
                ('department', models.CharField(max_length=255, null=True)),
                ('email_id', models.CharField(max_length=255, null=True)),
                ('student_id', models.CharField(max_length=100, null=True)),
                ('admin_id', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='serial_no',
        ),
        migrations.AddField(
            model_name='candidate',
            name='rank',
            field=models.IntegerField(null=True),
        ),
    ]
