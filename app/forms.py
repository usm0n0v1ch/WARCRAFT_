from django import forms

from app.models import Screenshot, Video, Audio


class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = Screenshot
        fields = ['image']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = '__all__'