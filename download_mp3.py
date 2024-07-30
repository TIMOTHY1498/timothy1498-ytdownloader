from pytubefix import YouTube
from pytubefix.cli import on_progress
import os
from time import sleep

url_input = input("Please input URL >>> ")
url = url_input

 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title+" is already decoded")
 
ys = yt.streams.get_audio_only()
result = ys.download(mp3=True) # pass the parameter mp3=True to save in .mp3
print("Downloading...")

base, ext = os.path.splitext(result)
new_MP3_file = base + '.mp3'
os.rename(result, new_MP3_file)
print("Downloading... Done")


sleep(2)
print("Exiting Process")
