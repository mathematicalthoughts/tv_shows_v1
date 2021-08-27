from django.db import models

# Create your models here.

class TVShow(models.Model):
    
    title = models.CharField(max_length=100)
    network = models.CharField(max_length=50)
    released_date = models.DateField()
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title}"