import re
from pytube import YouTube

# Function to sanitize file names
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

# Function to download the audio of a YouTube video
def download_audio(youtube_url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)

        # Get the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        
        # Sanitize the file name
        sanitized_title = sanitize_filename(yt.title)

        # Download the audio stream
        print(f"Downloading audio from: {yt.title}")
        audio_stream.download(output_path=output_path, filename=f"{sanitized_title}.mp3")
        print(f"Download complete! Audio saved to: {output_path}/{sanitized_title}.mp3")

    except Exception as e:
        print(f"An error occurred: {e}")

# Function to download the highest quality video of a YouTube video
def download_high_quality_video(youtube_url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(youtube_url)

        # Get the highest resolution video stream
        video_stream = yt.streams.get_highest_resolution()
        
        # Sanitize the file name
        sanitized_title = sanitize_filename(yt.title)

        # Download the video stream
        print(f"Downloading video: {yt.title}")
        video_stream.download(output_path=output_path, filename=f"{sanitized_title}.mp4")
        print(f"Download complete! Video saved to: {output_path}/{sanitized_title}.mp4")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
youtube_url = input('Enter YouTube link you want to download: ')
output_path = input('Enter path to download: ')

print('Type "video" for downloading video of that YouTube url\n Type "audio" for downloading audio of that YouTube url..\nType "both" for downloading both of them..')
a = input()

if a == 'video':
    download_high_quality_video(youtube_url, output_path)
elif a == 'audio':
    download_audio(youtube_url, output_path)
elif a == 'both':
    download_high_quality_video(youtube_url, output_path)
    download_audio(youtube_url, output_path)
