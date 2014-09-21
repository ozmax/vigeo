from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name


class Lesson(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()


class Question(models.Model):
    
    class Meta:
        permissions = (
            ("view_admin", "Can see admin pages"),
            )

    title = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=100)
    possible_answer0 = models.CharField(max_length=100)
    possible_answer1 = models.CharField(max_length=100)


class Student(models.Model):
     
    user = models.OneToOneField(User)
    test_data = models.CharField(max_length=100)
