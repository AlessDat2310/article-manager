from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name