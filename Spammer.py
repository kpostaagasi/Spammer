import time
import pyautogui
time.sleep(5)
f = open("joker", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(0.2)
