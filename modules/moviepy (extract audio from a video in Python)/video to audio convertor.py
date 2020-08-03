import moviepy.editor
video=moviepy.editor.VideoFileClip(input('Enter video file name ex- 1.mp4 : '))
audio=video.audio
audio.write_audiofile(input('to save Enter audio file name ex- 1.mp3 : '))