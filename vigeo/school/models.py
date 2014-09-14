from django.db import models

class Question(models.Model):
    
    title = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=100)
    possible_answer0 = models.CharField(max_length=100)
    possible_answer1 = models.CharField(max_length=100)


    class Meta:
        permissions = (
            ("view_admin", "Can see admin pages"),
            )
