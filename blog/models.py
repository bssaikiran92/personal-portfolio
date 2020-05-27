from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='')
    created_date = models.DateField()

    def __str__(self):
        return self.title
