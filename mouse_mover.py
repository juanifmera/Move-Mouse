import pyautogui as pag
import time
import random

while True:
    x = random.randint(900, 1500)
    y = random.randint(400, 800)
    pag.moveTo(x, y, 0.5)
    time.sleep(30)