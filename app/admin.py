from django.contrib import admin

from app.models import Screenshot, Video, Audio, ProcessOrCinematic, ReplicaOrSong

# Register your models here.

admin.site.register([Screenshot, Video, Audio, ProcessOrCinematic, ReplicaOrSong])