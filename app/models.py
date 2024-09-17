from django.db import models

# Create your models here.


class Screenshot(models.Model):
    image = models.ImageField(upload_to='screenshot_images')

class ProcessOrCinematic(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Video(models.Model):
    video = models.FileField(upload_to='video_files')
    process_or_cinematic = models.ForeignKey(ProcessOrCinematic, on_delete=models.CASCADE, blank=True, null=True)


class ReplicaOrSong(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
class Audio(models.Model):
    audio = models.FileField(upload_to='audio_files')
    replica_or_song = models.ForeignKey(ReplicaOrSong, on_delete=models.CASCADE, blank=True, null=True)
