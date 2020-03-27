import numpy as np
import cv2
from Color_Detector import ColorDetector

# Main programm
img_path = "./pictures/Blauer_Stein.jpg "
image_orginal = cv2.imread(img_path)
image = cv2.cvtColor(image_orginal,cv2.COLOR_BGR2HSV)
detector = ColorDetector()

if detector.detect_Red_Color(image):
    print("Der Legostein hat die Farbe Rot!")
elif detector.detect_Green_Color(image):    
    print("Der Legostein hat die Farbe Grün!")
elif  detector.detect_Blue_Color(image):   
    print("Der Legostein hat die Farbe Grün!")   
else                                    :
    print("Die Farbe des Stein wurde nicht erkannt.")    
