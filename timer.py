import time,pygame
def timer(end):
    for i in reversed(range(1,end+1)):
        print(i)
        time.sleep(1)
    print('TIME UP!!!!')
def sound():
    sound_file = 'MY PROJECTS/extras/Apple_iPhone_-_Alarm_Radar_Remix_(mp3.pm).mp3'
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    if pygame.mixer.music.get_busy():
        time.sleep(10)
timer(end=int(input('Enter the time in seconds: ')))
sound()