import youtube_dl

# Ask the user for the URL of the YouTube video
video_url = input("Enter the URL of the YouTube video you want to download: ")

# Set the desired audio format and the path where the audio file should be saved
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "audio.mp3"
}

# Use youtube_dl to download the audio from the video
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])
