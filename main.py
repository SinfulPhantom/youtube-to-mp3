import sys
from pytube import YouTube


def progress(stream, chunk, bytes_remaining) -> None:
    total_size = stream.filesize
    bytes_download = total_size - bytes_remaining
    percentage_of_completion = bytes_download / total_size * 100
    print(f"Download {percentage_of_completion} complete")


def download_mp3(url, path) -> None:
    youtube = YouTube(url)
    youtube.register_on_progress_callback(progress)
    audio_stream = youtube.stream_filter(only_audio=True).first()
    audio_stream.download(path)
    print(f"Downloaded audio: {youtube.title} has completed")


if __name__ == '__main__':
    video_url = sys.argv[1]
    output_path = 'C:\Users\xiad9\Downloads'
    download_mp3(video_url, output_path)
