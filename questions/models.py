from django.db import models

# Create your models here.


class Question(models.Model):
    content = models.CharField(max_length=200)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    count = models.IntegerField()


class Comment(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
