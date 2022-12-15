from pytube import YouTube

# Set the URL of the YouTube video you want to download
video_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Use pytube to download the audio from the video
yt = YouTube(video_url)
audio = yt.streams.filter(only_audio=True).first()
audio.download()
