"""
URL configuration for AIVoiceRecorderProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# AIVoiceRecorderProject/urls.py
from AIAudioStorageProject.views import index, upload_audio, upload_success, save_audio, upload_to_s3
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('upload/', upload_audio, name='upload_audio'),
    path('upload_success/', upload_success, name='upload_success'),
    path('save_audio/', save_audio, name='save_audio'),
    path('upload_to_s3/', upload_to_s3, name='upload_to_s3'),
]





