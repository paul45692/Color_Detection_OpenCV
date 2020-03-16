import cv2
import numpy as np
# Load the image
img_path = "./pictures/Train_Example.jpg"
image = cv2.imread(img_path)
# Convert the picture into hsv
image_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
# Define the color range in the HSV color space
ranges = {
        "Red": ([161, 155, 84], [179, 255, 255]),
        "Green": ([46, 52, 72],[100, 255, 255]),
        "Blue": ([101, 50,0],[140,255,255]),
}
# Processing
for key in ranges.keys():
    lowerRange = np.array(ranges[key][0], dtype="uint8")
    upperRange = np.array(ranges[key][1], dtype="uint8")
 
 
    mask = cv2.inRange(image_hsv, lowerRange, upperRange)
    output = cv2.bitwise_and(image_hsv, image, mask=mask)
 
    # show the images
    cv2.imshow(key, output)
    # Leave key is 
    cv2.waitKey(0)
cv2.destroyAllWindows()