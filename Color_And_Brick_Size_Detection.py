import numpy as np
import cv2

from Color_Detector import ColorDetector
from Contours_Detector import ContourDetector

def detect_Any_Color_In_the_Image(img_org):
    detector = ColorDetector()
    if detector.detect_Red_Color(img_org):
        color = "red"
    elif detector.detect_Green_Color(img_org):
        color ="green"
    elif detector.detect_Blue_Color(img_org):
        color = "blue"        
    else:
        color= "No color detected!"
    return color

# Main program
img_path_small = './pictures/Legostein_small.jpg'
img_path_big  = './pciture/Blauer_Legostein.jpg'
# Load the images
img_small = cv2.imread(img_path_small)
img_big = cv2.imread(img_path_big)
print("Detecting the color of the bricks:")
color_small = detect_Any_Color_In_the_Image(img_small)
color_big = detect_Any_Color_In_the_Image(img_big)
print("The first bick is" + color_small)
print("The second bick is" + color_big)
# Detecting the size of the bricks
contours = ContourDetector()
print("Detecting the size of the bricks:")
number_of_contours_small = contours.calculate_Numbers_of_Contours_In_a_image(img_small)
number_of_contours_big = contours.calculate_Numbers_of_Contours_In_a_image(img_big)
print("The first brick has a " + color_small + " and" + contours.calculate_Brick_Size(number_of_contours_small))
print("The second brick has a " + color_big + " and" + contours.calculate_Brick_Size(number_of_contours_big))
