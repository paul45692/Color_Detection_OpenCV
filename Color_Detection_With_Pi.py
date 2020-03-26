from picamera import PiCamera
from time import sleep
from Color_Detector import *
import cv2

    # This function only works with the raspberry Pi Camera
def takePictureWithPi(image_name):
    camera = PiCamera()
    camera.start_Preview()
    sleep(3)
    camera.capture('home/pi/Desktop/'+ image_name + '.jpg')
    camera.stop()
    print("The image was taken!")
# Main program
image_name = "test"
# Take the picture with the pi camera
takePictureWithPi(image_name)
img_path = 'home/pi/Desktop/' + image_name + '.jpg'
image_orginal = cv2.imread(img_path)
image = cv2.cv2.cvtColor(image_orginal,cv2.COLOR_BGR2HSV)
detector = Color_Detector()
# Detecting the color in the image
if detector.detect_Red_Color(image):
    print("Der Legostein hat die Farbe Rot!")
elif dectector.detect_Green_Color(image):    
    print("Der Legostein hat die Farbe Grün!")
elif  dectector.detect_Blue_Color(image):   
    print("Der Legostein hat die Farbe Grün!")   
else                                    :
    print("Die Farbe des Stein wurde nicht erkannt.")    




