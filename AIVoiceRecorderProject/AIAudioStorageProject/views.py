# AIAudioStorageProject/views.py
from botocore.exceptions import NoCredentialsError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import AudioFileForm
import io
import boto3


def convert_to_wav(audio_file, sf=None):
    # Чтение аудиофайла и конвертация в WAV формат
    audio_data = audio_file.read()
    wav_data = io.BytesIO()
    sf.write(wav_data, audio_data, samplerate=44100, format='WAV')
    wav_data.seek(0)
    return wav_data.read()

def save_audio(request):
    if request.method == 'POST' and 'audio_data' in request.FILES:
        audio_file = request.FILES['audio_data']

        # Конвертируем аудиофайл в WAV формат
        wav_data = convert_to_wav(audio_file)

        # Отправляем WAV файл на Amazon S3
        s3_client = boto3.client('s3', region_name='')  # Укажите свой регион
        bucket_name = 'voiseproject'  # Укажите имя вашего бакета
        file_key = 'audio.wav'  # Укажите ключ (путь) для сохранения файла на S3
        s3_client.put_object(Body=wav_data, Bucket=bucket_name, Key=file_key)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error'}, status=400)

def index(request):
    return render(request, 'index.html')
