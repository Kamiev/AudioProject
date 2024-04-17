# AIAudioStorageProject/models.py

from django.db import models

class AudioFile(models.Model):
    name = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
