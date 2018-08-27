from PIL import ImageGrab,ImageOps
import pyautogui
import time
from numpy import *

class cordinates():
    replayBtn=(440,375)#this are the coordinates of the replay button on the screen detected by paint.net
    dinosaur=(185,400)
    #380 is the y coordinate of the smallest tree

def restartGame():
    pyautogui.click(cordinates.replayBtn)
    #pyautogui.keyDown('down')

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.18)#time for which the spacebar is presseds
    pyautogui.keyUp('space')

def imageGrab():
    box =(cordinates.dinosaur[0]+50,cordinates.dinosaur[1],cordinates.dinosaur[0]+90,cordinates.dinosaur[1]+32)
    image = ImageGrab.grab(box)
    grayImage =ImageOps.grayscale(image)
    a= array(grayImage.getcolors())
    return a.sum()#this array helps us to detect the change in colour at some particular point
def main():
    restartGame()
    while True:
        print(imageGrab() )
        if(imageGrab()!=1527):#the sum of the array may change on varrying the screen coordinates
            pressSpace()
            time .sleep(0.18)
main()



