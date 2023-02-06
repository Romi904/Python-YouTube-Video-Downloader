import pytube

link = input("Enter the link of YouTube video you want to download: ")
yt = pytube.YouTube(link)

# yt.streams.get_highest_resolution().download()

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()

# yt.streams.filter(res="720p").first().download()

print('Video downloaded successfully',link)