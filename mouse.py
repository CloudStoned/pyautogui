
import pyautogui
import time

time.sleep(3)

# MOVEREL KUNG NASAN UNG MOUSE POINTER YUN YUNG INITIAL LOCATION NG GAGAWIN

print(pyautogui.size()) # RESO
# print(pyautogui.position())
# pyautogui.moveTo(100,100,1)
# pyautogui.moveRel(200,20,1)
# pyautogui.leftClick()
# pyautogui.rightClick()
# pyautogui.tripleClick()
# pyautogui.doubleClick()

# pyautogui.scroll(300)
# pyautogui.scroll(-300)

pyautogui.mouseDown(300,400, button="left") # CLICK HOLDER
pyautogui.moveTo(800, 400, 3)
pyautogui.moveRel(800,-420,3)

# pyautogui.mouseUp() RELEASE CLICK HOLDER
