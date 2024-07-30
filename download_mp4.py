from pytubefix import YouTube
from pytubefix.cli import on_progress
from time import sleep
import os

url_input = input("Please input URL >>> ")
url = url_input
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title+" is already decoded")

ys = yt.streams.get_highest_resolution()
result = ys.download()
print("Downloading...")

base, ext = os.path.splitext(result)
new_MP3_file = base + '.mp4'
os.rename(result, new_MP3_file)
print("Downloading... Done")
sleep(2)
print("Exiting Process")

