from pytube import YouTube

print('\nDownTube by GoomesH - SCRIPT Projected based on PyTube\n')

youtube = input('insert URL of your video here:\n')

print('Please, wait a minute...\n')

youtube = YouTube(youtube)

youtube.streams.get_highest_resolution().download()

print('Your video is here! Take a look at the project folder! \n')
