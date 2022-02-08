from email import message
from logging import exception
from turtle import position
import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(2)

position1=pt.locateOnScreen("E:\Projects\Python\Whatsapp Bot\Whatsapp\Screenshot (80).png", confidence=.6)
x = position1[0]
y = position1[1]

#GET_MESSAGE
def get_message():
    global x, y

    position = pt.locateOnScreen("E:\Projects\Python\Whatsapp Bot\Whatsapp\Screenshot (80).png", confidence=.6)
    x= position[0]
    y= position[1]
    pt.moveTo(x,y, duration=.5)
    pt.moveTo(x+37,y-40,duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()
    whatsapp_message= pyperclip.paste()
    pt.click()
    print("Messaage received: "+ whatsapp_message)

    return whatsapp_message
#Posts
def post_response(message):
    global x,y

    position=pt.locateOnScreen("E:\Projects\Python\Whatsapp Bot\Whatsapp\Screenshot (80).png", confidence=.6)
    x= position[0]
    y= position[1]
    pt.moveTo(x+200,y,duration=.5)
    pt.click()
    pt.typewrite(message, interval=.01)

    pt.typewrite("\n",interval=.01)
#processes response
def process_response(message):
    random_no=random.randrange(3)
    if "?" in str(message).lower():
        return "Dont't ask me any questions!"
    else:
        if random_no==0:
            return "That's cool!"
        elif random_no==1:
            return "I'm very hungry right now!"

#Check For New Messages
def check_for_new_messages():
    pt.moveTo(x+40,y-30,duration=.05)
    while True:
        #continuously checks for new dot
        try:
            position=pt.locateOnScreen("E:\Projects\Python\Whatsapp Bot\Whatsapp\Screenshot (81).png",confidence=.7)
            if position  is not None:
                pt.moveTo(position)
                pt.moveRel(-100,0)
                pt.click()
                sleep(.5)
        except(exception):
            print("No other user with new message located!")
        if pt.pixelMatchesColor(int(x+40),int(y-30),(255,255,255),tolerance=18):
            print("It's White!")
            processed_message=process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet!")
        sleep(5)

#processed_message=process_response(get_message())
#post_response(processed_message)
check_for_new_messages()

