from django.db import models

# Create your models here.

class Video(models.Model):
    video = models.FileField(upload_to='videos/')
    created_at = models.DateTimeField(auto_now_add=True)
    transcription = models.URLField(max_length=256, null=True, blank=True)

    def __str__(self) -> str:
        return self.video