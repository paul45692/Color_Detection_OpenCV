import cv2
import numpy as np
# This class checks if the image contains a specific color like red, green or blue
class ColorDetector:
    
    def detect_Red_Color(self, image):
        # Define ranges for the blue color
        lowerRange = np.array([160, 155, 84])
        upperRange = np.array([179, 255, 255])
        return cv2.inRange(image, lowerRange, upperRange).any()

    def detect_Green_Color(self, image):
        # Define ranges for the blue color
        lowerRange = np.array([46, 52, 72])
        upperRange = np.array([100, 255, 255])
        return cv2.inRange(image, lowerRange, upperRange).any()

    def detect_Blue_Color(self, image):
        # Define ranges for the blue color
        lowerRange = np.array([100, 50,0])
        upperRange = np.array([140,255,255])
        return cv2.inRange(image, lowerRange, upperRange).any()
