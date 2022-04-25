from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField()
    time_create = models.DateTimeField()
    time_changed = models.DateTimeField()
    name = models.CharField(max_length=150)
    group = models.CharField(max_length=50)
    member_gz_2021_2022 = models.CharField(max_length=10, blank=True)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    marital_status = models.CharField(max_length=20)
    living = models.CharField(max_length=50)
    children = models.CharField(max_length=20)
    work_status = models.CharField(max_length=50)
    working_in_fishing_or_shipping = models.CharField(max_length=30)
    working_maritime = models.CharField(max_length=30)
    working_fishing_industry = models.CharField(max_length=30)
    working_fishing_technology = models.CharField(max_length=30, blank=True)
    working_aquaculture = models.CharField(max_length=30, blank=True)
    working_economic = models.CharField(max_length=30, blank=True)
    working_it = models.CharField(max_length=30, blank=True)
    working_other = models.CharField(max_length=30, blank=True)


class Question(models.Model):
    text_question = models.TextField()


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50, blank=True, null=True)
