import pyautogui
import  time
import  math


time.sleep(2)
pyautogui.moveTo(580,369,1)
# pyautogui.dragRel(0,100,1)
# pyautogui.moveTo(580,369,1)
# pyautogui.dragRel(20,95,1)
# pyautogui.moveTo(580,369,1)
# pyautogui.dragRel(40,80,1)
radius = 100
center_x = 580
center_y = 369

angle = 0
while angle <= 360:
    # Calculate the new position on the circle using trigonometry
    x = int(center_x + radius * math.cos(math.radians(angle)))
    y = int(center_y + radius * math.sin(math.radians(angle)))

    # Move the mouse to the new position
    pyautogui.dragTo(x, y)

    # Increment the angle for the next position
    angle += 5


# while True:
#     print(pyautogui.position())