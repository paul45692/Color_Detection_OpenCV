import cv2
import numpy as np

class ContourDetector:

    def display_Contours_In_the_image(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges_images = cv2.Canny(gray_image ,100,200)
        image, contours, hierarchy = cv2.findContours(edges_images,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
        cv2.imshow('Picture with Contours', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def calculate_Numbers_of_Contours_In_a_image(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges_images = cv2.Canny(gray_image ,100,200)
        image, contours, hierarchy = cv2.findContours(edges_images,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        number_of_contours = len(contours)

        return number_of_contours

    def calculate_Brick_Size(self, number_of_contours):
        if number_of_contours >= 10:
            print("has the size of 2 x 4 !")
        else:
            print(" has the size of 2 x 2 !")    