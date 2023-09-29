from django.db import models

# Create your models here.

class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.video