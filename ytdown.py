from pytubefix import YouTube
from pytubefix.cli import on_progress

url = "https://youtu.be/AtW0E5BbMDc?si=z3CM4iKeF6UpVQdK"

yt = YouTube(url, on_progress_callback=on_progress)

# ys = yt.streams.get_highest_resolution().resolution
# print(yt.streams.filter(file_extension='mp4', progressive=True))
ys = yt.streams.filter(file_extension='mp4')
print(ys)
ys.get_by_itag(136).download()
