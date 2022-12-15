from pytube import YouTube

# Ask the user for the URL of the YouTube video
video_url = input("Enter the URL of the YouTube video you want to download: ")

# Use pytube to download the audio from the video
yt = YouTube(video_url)
audio = yt.streams.filter(only_audio=True, file_extension="mp3").first()
audio.download()
