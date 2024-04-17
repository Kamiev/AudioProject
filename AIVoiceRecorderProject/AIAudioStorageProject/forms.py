# AIAudioStorageProject/forms.py

from django import forms
from .models import AudioFile

class AudioFileForm(forms.ModelForm):
    class Meta:
        model = AudioFile
        fields = ['name', 'audio_file']
