import pyautogui
import time

channel = pyautogui.prompt(text="",title="Enter Channel Name: ")
print(channel)

pyautogui.hotkey("ctrl","t")
pyautogui.write("https://www.youtube.com/")
pyautogui.press("enter")
pyautogui.moveTo(676,130,1)
pyautogui.click()
time.sleep(1)
pyautogui.write(channel)
pyautogui.press("enter")
