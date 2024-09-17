from django.urls import path

from app import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('screenshots/', views.screenshots, name='screenshots'),
    path('video/', views.video, name='video'),
    path('audio/', views.audio, name='audio'),
    path('add/', views.add, name='add'),
    path('show_screenshot/', views.show_screenshot, name='show_screenshot'),
    path('screenshots/delete/<int:screenshot_id>/', views.delete_screenshot, name='delete_screenshot'),
    path('edit_screenshot/<int:screenshot_id>/', views.edit_screenshot, name='edit_screenshot'),
    path('show_video/', views.show_video, name='show_video'),
    path('videos/<int:video_id>/delete/', views.delete_video, name='delete_video'),
    path('videos/<int:video_id>/edit/', views.edit_video, name='edit_video'),
    path('show_audio/', views.show_audio, name='show_audio'),
    path('audios/<int:audio_id>/delete/', views.delete_audio, name='delete_audio'),
    path('audios/<int:audio_id>/edit/', views.edit_audio, name='edit_audio'),
    path('add_screenshot/', views.add_screenshot, name='add_screenshot'),
    path('add_video/', views.add_video, name='add_video'),
    path('add_audio/', views.add_audio, name='add_audio'),
]
