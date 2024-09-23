import yt_dlp
import re

# Function to sanitize file names
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "_", name)

# Function to download YouTube content
def download_youtube_content(youtube_url, output_path, download_type='both'):
    try:
        # Set options for yt-dlp
        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'noplaylist': True,
            'quiet': False
        }

        if download_type == 'both':
            # Download audio
            ydl_opts['format'] = 'bestaudio/best'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=True)
                print(f"Audio downloaded: {info['title']}.mp4")
            
            # Download video
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
            ydl_opts['outtmpl'] = f'{output_path}/%(title)s_video.%(ext)s'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=True)
                print(f"Video downloaded: {info['title']}_video.mp4")
        
        elif download_type == 'audio':
            # Download audio
            ydl_opts['format'] = 'bestaudio/best'
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(youtube_url, download=True)
                print(f"Audio downloaded: {info['title']}.mp4")

        elif download_type == 'video':
            # Download video
            ydl_opts['format'] = 'bestvideo+bestaudio/best'
            ydl_opts['outtmpl'] = f'{output_path}/%(title)s_video.%(ext)s'
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(youtube_url, download=True)
                    print(f"Video downloaded: {info.get('title')}_video.mp4")
            except Exception as e:
                print(f"An error occurred: {str(e)}")


        else:
            print("Invalid option selected. Please type 'video', 'audio', or 'both'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

logo = r"""
                                   _________
           /\       |    /   o     |
          /  \      |  /     |     |
         /____\     |/       |     |____
        /      \    |  \     |     |
  by   /        \   |    \   |     |

    YOUTUBE DOWNLOADER
"""
print(logo)

# Example usage
youtube_url = input('Enter YouTube link you want to download: ')
output_path = input('Enter path to download: ')

print('Type "video" for downloading video of that YouTube URL\nType "audio" for downloading audio of that YouTube URL\nType "both" for downloading both of them..')
a = input().strip().lower()

download_youtube_content(youtube_url, output_path, download_type=a)
