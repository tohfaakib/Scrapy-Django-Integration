from django.db import models

# Create your models here.


class Quotes(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=100)
    tags = models.CharField(max_length=255)

    def __str__(self):
        return self.quote
