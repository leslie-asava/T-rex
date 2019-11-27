from pynput.keyboard import Key, Listener
import datetime
import pyautogui
import PIL
import time
input("Press Enter key to start capturing images for your dataset...")

player_left, player_top, player_width, player_height = pyautogui.locateOnScreen("player.png")
frame_location = (player_left+36, player_top,player_left+150,player_top+player_height)

def on_press(key):
    filename = str(datetime.datetime.today())
    filename = filename.replace(" ","")
    filename = filename.replace(":","")
    filename = filename.replace(".","")
    filename+=".png"
    if key == Key.up:
        print("Jump")
        image = PIL.ImageGrab.grab(frame_location)
        image.save("Jump\\"+filename)
def on_release(key):
    filename = str(datetime.datetime.today())
    filename = filename.replace(" ","")
    filename = filename.replace(":","")
    filename = filename.replace(".","")
    filename+=".png"
    if key == Key.up:
        time.sleep(0.1)
        image = PIL.ImageGrab.grab(frame_location)
        image.save("Stay\\"+filename)


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
