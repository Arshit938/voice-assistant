import keyboard
import time
from Assistant import assistant
while True:
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('a'):
        print('active')
        assistant()
        break
    time.sleep(0.02)





