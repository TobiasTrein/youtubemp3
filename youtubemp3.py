import sys
import yt_dlp

def download_best_audio(youtube_url):
    # Opções de download para obter o áudio na melhor qualidade
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python youtubemp3.py <link do vídeo>")
    else:
        youtube_link = sys.argv[1]
        download_best_audio(youtube_link)
