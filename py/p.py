
import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)

position1 = pt.locateOnScreen("pin.png", confidence=.6)
x = position1[0]
y = position1[1]


def get_message():
    global x,y

    postion = pt.locateOnScreen("pin.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x + 50, y - 50, duration = .5)
    pt.click(clicks=3)
    pt.rightClick()
    pt.moveRel(13,13)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print("message received: " + whatsapp_message)

    return whatsapp_message


def post_response(message):
    global x, y

    position = pt.locateOnScreen("pin.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 30, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n", interval=.01)


def process_response(message):
    random_no = random.randrange(3)

    if "?"in str(message).lower():
        return "Interesting question, I'll talk to you about that later - edith"

    else:
        if "hi"in str(message).lower():
            return "Hey, a bit busy right now. just drop a message ill talk to you later- edith"
        elif "happy new year"in str(message).lower():
            return "Wishing you and your family a very Happy New Year! ✨.May this year bring joy and happiness in your life! - edith "
        elif "good morning"in str(message).lower():
            return"Good Morning! Have a great day"
        elif "good night"in str(message).lower():
            return"Good Night! Sleep tight"
        else :
            return "Hello! Dear Sir/Madam, Naveen is currently unavailable to reply. Do drop your messages. - edith "
            

def read():
    pt.moveTo(x + 17, y - 35, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("UNREAD.png", confidence = .7)

            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                processed_message = process_response(get_message())
                post_response(processed_message)
                sleep(5)

            else:
                print("No messages")
                sleep(5)
        except(Exception):
            print("No new messages")
read()