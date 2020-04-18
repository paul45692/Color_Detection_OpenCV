# Color_Detection_OpenCV
This project has the goal to detect the color of a lego bricks and classify the
brick by the size.

Solution:

A. Problem of color
- Convert the image into the hsv color space and uses a threshold for each color.
   By performing the mask operation on the image we can detect if the a specific color
   e.g. blue is in the image or not.

B. Problem of classify the bricks by the brick size
- Simple approach for detecting if the brick has the size 2 x 2 or 2 x 4.
- Step 1: Convert the image into a grayed image for better processing performances
- Step 2: Perform edge detection with cv2.canny()
- Step 3: Based on the edges in the image perform contours detection in the image
- Step 4: Calculate the number of contours in the image:
    - For the size 2 x 4 the image contains more than ten contours -> Big brick
    - For the size 2 x 2 the image contains less than 5 contours -> Small brick
