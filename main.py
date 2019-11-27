import os
import pyautogui
import PIL
import numpy as np
import tensorflow as tf
import pickle
import cv2
import time

# Load saved model
model = tf.keras.models.load_model("brain.model")
CATEGORIES = ["Jump","Stay"]
os.system("cls")
os.system("color a")
print(r"""
                            + + REX + +
               """)
input("[*] Loaded 'brain.model'\n[+] Press Enter key to continue ")

# Find player location to use as reference point
player_left, player_top, player_width, player_height = pyautogui.locateOnScreen("player.png")
# Define the screen portion the bot will be watching relative to the player
frame_location = (player_left+35, player_top,player_left+149,player_top+player_height)

input("[*] Player located \n[+] Press Enter key to start ")

# Click somewhere in the window to make it active
pyautogui.click(player_left,player_top-50)
pyautogui.keyDown("space")

while True:
    state = PIL.ImageGrab.grab(frame_location)
    state = cv2.cvtColor(np.array(state), cv2.COLOR_RGB2BGR)
    state = cv2.cvtColor(state,cv2.COLOR_BGR2GRAY)
    state = cv2.resize(state,(57,19))
    state = np.reshape(state,(1,57,19,1))
    prediction=np.argmax(model.predict(state))
    if (CATEGORIES[prediction]) == "Jump":
        pyautogui.keyDown("space")
        time.sleep(0.03)
        pyautogui.keyUp("space")
        print("Prediction : "+CATEGORIES[prediction])
        
input("Press Enter key to exit...")
