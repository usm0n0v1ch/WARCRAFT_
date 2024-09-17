from django.shortcuts import render, get_object_or_404, redirect

from app.forms import ScreenshotForm, VideoForm, AudioForm
from app.models import Screenshot, Video, Audio


# Create your views here.


def about(request):
    return render(request, 'app/about.html')

def screenshots(request):
    screenshots = Screenshot.objects.all()
    ctx = {'screenshots': screenshots}
    return render(request, 'app/screenshots.html', ctx)

def video(request):
    videos = Video.objects.all()
    ctx = {'videos': videos}
    return render(request, 'app/video.html',ctx)

def audio(request):
    audios = Audio.objects.all()
    ctx = {'audios': audios}
    return render(request, 'app/audio.html', ctx)

def add(request):
    return render(request, 'app/add.html')

def show_screenshot(request):
    screenshots = Screenshot.objects.all()
    ctx ={
        'screenshots': screenshots
    }
    return render(request, 'app/show_screenshot.html',ctx)


def delete_screenshot(request, screenshot_id):
    screenshot = get_object_or_404(Screenshot, id=screenshot_id)
    if request.method == 'POST':
        screenshot.delete()
        return redirect('show_screenshot')
    return render(request, 'app/confirm_delete.html', {'screenshot': screenshot})


def edit_screenshot(request, screenshot_id):
    screenshot = get_object_or_404(Screenshot, id=screenshot_id)

    if request.method == 'POST':
        form = ScreenshotForm(request.POST, request.FILES, instance=screenshot)
        if form.is_valid():
            form.save()
            return redirect('show_screenshot')
    else:
        form = ScreenshotForm(instance=screenshot)

    return render(request, 'app/edit_screenshot.html', {'form': form, 'screenshot': screenshot})


def edit_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)

    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            form.save()
            return redirect('show_video')
    else:
        form = VideoForm(instance=video)

    return render(request, 'app/edit_video.html', {'form': form, 'video': video})


def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    if request.method == 'POST':
        video.delete()
        return redirect('show_video')


def show_video(request):
    videos = Video.objects.all()
    return render(request, 'app/show_video.html', {'videos': videos})



def show_audio(request):
    audios = Audio.objects.all()
    return render(request, 'app/show_audio.html', {'audios': audios})


def delete_audio(request, audio_id):
    audio = get_object_or_404(Audio, id=audio_id)
    if request.method == 'POST':
        audio.delete()
        return redirect('show_audios')


def edit_audio(request, audio_id):
    audio = get_object_or_404(Audio, id=audio_id)

    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES, instance=audio)
        if form.is_valid():
            form.save()
            return redirect('show_audios')
    else:
        form = AudioForm(instance=audio)

    return render(request, 'app/edit_audio.html', {'form': form, 'audio': audio})


def add_screenshot(request):
    if request.method == 'POST':
        form = ScreenshotForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_screenshot')
    else:
        form = ScreenshotForm()

    return render(request, 'app/add_screenshot.html', {'form': form})

def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_video')
    else:
        form = VideoForm()

    return render(request, 'app/add_video.html', {'form': form})

def add_audio(request):
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show_audio')
    else:
        form = AudioForm()

    return render(request, 'app/add_audio.html', {'form': form})