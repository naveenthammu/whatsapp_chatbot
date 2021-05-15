import pyautogui as p
from time import sleep
while True:
    posxy=p.position()
    print(posxy)
    
    if posxy[0]==0:
        break