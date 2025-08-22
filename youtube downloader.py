import yt_dlp
import os
def download_youtube_audio(url, output_dir='downloads'):
    os.makedirs(output_dir,exist_ok=True)
    ydl_opts = {
        
        'format': 'bestaudio/best',
        'postprocessors':[{
            
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }], 
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'retries': 3,

    } 
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url,download=True)
            print(f"\nDownloaded: {info['title']}")
            return os.path.join(output_dir, f"{info['title']}.mp3")
    except Exception as e :
        print(f"\n Error downloading audio: {e}")
        return None
if __name__ == "__main__":
    video_url = input("Enter youtube URL: ").strip()
    download_path = download_youtube_audio(video_url)

    if download_path: 
        print(f"Audio saved to {download_path}")
    else:
        print("Downlaod Failed. Check your url")    
