# Imports
import cv2
import numpy as np

# Load the image
img_path = "./pictures/Blauer_Stein.jpg"
image = cv2.imread(img_path)
# Convert the picture into hsv
image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# Define the range of the blue color in hsv
lowerRange_blue = np.array([100,150,0])
upperRange_blue = np.array([140,255,255])
# Perform mask operation on the picture
mask = cv2.inRange(image_hsv, lowerRange_blue, upperRange_blue)
output = cv2.cv2.bitwise_and(image, image_hsv, mask=mask)
# Display the result
cv2.imshow('Blue',output)
cv2.waitKey(0)
cv2.destroyAllWindows()