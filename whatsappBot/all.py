import pyautogui as pt
from time import sleep
import pyperclip
import random
from PIL import ImageGrab
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("whatsappBot/db.sqlite3")

cur = con.cursor()

sleep(2)

position1 = pt.locateOnScreen("whatsappBOT/smiley_and_paperclip.PNG", confidence = .6)
if position1 is not None:
    x = position1[0]
    y = position1[1]
else:
    x=0
    y=0

#Get Message
def get_message():
    global x, y
    position = pt.locateOnScreen("whatsappBOT/smiley_and_paperclip.PNG", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x+90, y-50, duration=0.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12, 15)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()
    print(whatsapp_message)
    return whatsapp_message


def post_response(message):
    global x, y
    position = pt.locateOnScreen("whatsappBOT/smiley_and_paperclip.PNG", confidence = .6)
    x = position[0]
    y = position[1]
    pt.moveTo(x+200, y+20, duration=.5)
    pt.click()
    pt.typewrite(message, interval=0.01)
    pt.typewrite("\n", interval=0.01)



# process response
def process_response(message):
    random_no = random.randrange(4)

    if "hi" in str(message).lower():
        cur.execute('SELECT * FROM home_post;')
        c = cur.fetchall()
        print(cur.fetchall())
        print(c)
        return str(c[0][1])
    
    if "?" in str(message).lower():
        return "Don't ask me any question!"

    else:
        if random_no == 0:
            return "That's cool!"
        elif random_no==1:
            return "Remember that Tanya is the best!"
        elif random_no==2:
            return "Raghav is pagal"
        
        else:
            return "I hate you"


def check():
    pt.moveTo(x+100, y-32, duration=0.5)
    while True:
        #continuously check for green dot and message
        try:
            position = pt.locateOnScreen("whatsappBot/greendot.PNG", confidence = .7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(0.5)
        except(Exception):
            print("No new message")

        pixelRGB = ImageGrab.grab().getpixel((int(x+100), int(y-32)))
        print(pixelRGB)
        if pixelRGB == (38, 45, 49):
            print("is white")
            processed_message = process_response(get_message())
            post_response(processed_message)
        else:
            print("No new messages yet...")
        sleep(2)

check() 
# con.close()

