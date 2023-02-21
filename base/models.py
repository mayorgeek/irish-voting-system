from django.db import models

# Create your models here.


class Vote(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.CharField(max_length=100)
    voting_label = models.CharField(max_length=255)
    preferred_candidate = models.CharField(max_length=255)


# class Student(models.Model):
#     id = models.AutoField(primary_key=True)
#     student_id = models.CharField(max_length=100)
#     password = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     faculty = models.CharField(max_length=255)
#     department = models.CharField(max_length=255)
#     email_id = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True)
    faculty = models.CharField(max_length=255, null=True)
    department = models.CharField(max_length=255, null=True)
    email_id = models.CharField(max_length=255, null=True)
    student_id = models.CharField(max_length=100, null=True)
    admin_id = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=255)


# class Admin(models.Model):
#     id = models.AutoField(primary_key=True)
#     admin_id = models.CharField(max_length=100)
#     password = models.CharField(max_length=255)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)


class Candidate(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    rank = models.CharField(max_length=10, null=True)


class Voting(models.Model):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)


class Result(models.Model):
    id = models.AutoField(primary_key=True)
    voting_label = models.CharField(max_length=255)
    winner = models.CharField(max_length=255)



