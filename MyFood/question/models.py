from django.db import models


class QuestionModel(models.Model):
    name = models.TextField()
    email = models.EmailField()
    question = models.TextField()

