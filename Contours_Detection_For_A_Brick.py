import numpy as np
import cv2

# Main program

# Load the image
img_path = "/pictures/Roter_Legostein.jpg"
image = cv2.imread(img_path)
# Convert the image into a grayed image
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Apply edge detection on the image
edges_images = cv2.Canny(gray_image ,100,200)
# Showing the image
#cv2.imshow('Edges', edges_images)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

# Perform contours detection
ret,thresh = cv2.threshold(gray_image,100,255,0)
image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# Draw the contours into the image
output_image = cv2.drawContours(gray_image, contours, -1, (0,255,0), 3)
cv2.imshow('Contours', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()