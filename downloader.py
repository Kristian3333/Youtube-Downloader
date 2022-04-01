from pytube import YouTube

Links=[ 'https://www.youtube.com/watch?v=J63d-0HVISc']


for Link in Links:
    YouTube(Link).streams.first().download()
