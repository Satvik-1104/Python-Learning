import pyautogui
import time
time.sleep(2)
c = 0
while c < 50:
    pyautogui.typewrite("Hi, How are You?")
    c += 1
    pyautogui.press("enter")
