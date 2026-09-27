from django.db import models


class Question(models.Model):
    question = models.TextField()
    grade = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class Choice(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE
    )
    choice = models.TextField()
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice


class Submission(models.Model):
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return f"Submission {self.id}"
