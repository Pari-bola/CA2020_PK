from django.db import models

# Create models here.

class Blog(models.Model):
        subject=models.CharField(max_length=50)
        body = models.TextField(max_length=500)

        def __str__(self):
            return self.subject
