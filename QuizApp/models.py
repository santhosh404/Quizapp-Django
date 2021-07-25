from django.db import models

# Create your models here.

class Quizapplication(models.Model):
    question=models.TextField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_ans=models.CharField(max_length=100)
