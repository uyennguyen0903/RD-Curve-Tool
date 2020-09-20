import pytube
import os
import sys

for i in range(1, len(sys.argv)):
    url = sys.argv[i]
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()


print("Done!!!")