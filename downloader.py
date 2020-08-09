import pytube

for i in range(1, len(sys.argv)):
    url = argv[i]
    youtube = pytube.YouTube(url)
    video = youtube.streams.get_highest_resolution()
    video.download()


print("Done!!!")