import pyautogui as pt
from time import sleep
import pyperclip
import random
import os.path

# construct an absolute path to the directory this file is located in
HERE = os.path.dirname(os.path.abspath(__file__))

sleep(3)
image_path = os.path.join(HERE, 'smily.png')

position1 = pt.locateOnScreen(image_path, confidence=.8)

x = position1[0]
y = position1[1]


def get_message():
    global x, y

    position = pt.locateOnScreen(image_path, confidence=.7)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y)
    pt.moveTo(x + 81, y - 40, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_messgae = pyperclip.paste()
    pt.click()
    print("msg received:" + whatsapp_messgae)
    return whatsapp_messgae


def post_response(message):
    global x, y
    position = pt.locateOnScreen(image_path, confidence=.8)

    x = position[0]
    y = position[1]

    pt.moveTo(x + 200, y + 20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n",interval=.01)

def process_response(message):
    random_no = random.randrange(3)

    if "k" in str(message).lower():
        return "bye from bot"
    else:
        if random_no == 0:
            return "hi from bot"
        elif random_no == 1:
            return "hlo"
        else:
            return "bye"


def check_new_msgs():
    pt.moveTo(x + 81, y - 25, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("F:\softwares\whats_app_bot\whatsapp\green_dot.png", confidence=.9)


            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(2)

        except(Exception):
            print("no new messages")

        if pt.pixelMatchesColor(int(x + 81), int(y - 25), (255,255,255), tolerance=10):
            print("white")
            processed_msg = process_response(get_message())
            post_response(processed_msg)
        else:
            print("no new msgs")
        sleep(5)



check_new_msgs()

