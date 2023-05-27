from django.db import models


class Food(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()
    img_link = models.TextField()
    type = models.ForeignKey('Type', null=True, on_delete=models.PROTECT)


class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


