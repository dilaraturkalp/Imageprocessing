import cv2

# The draw_line function draws a line on an image from the given start to end points with the specified thickness and color.
def draw_line(img, start, end, color, thickness):
    # The set_pixel function sets a pixel at the given (x, y) coordinates with the specified thickness.
    def set_pixel(x, y):
        # If the pixel coordinates are within the image boundaries
        if 0 <= x < len(img[0]) and 0 <= y < len(img):
            # Set the pixels within the thickness
            for i in range(-thickness // 2, thickness // 2 + 1):
                for j in range(-thickness // 2, thickness // 2 + 1):
                    # If the (x + i, y + j) coordinates are within the image boundaries
                    if 0 <= x + i < len(img[0]) and 0 <= y + j < len(img):
                        # Color the pixels at these coordinates with the specified color
                        img[y + j][x + i] = color

    # Get the coordinates of the start and end points
    x1, y1 = start
    x2, y2 = end
    # Calculate delta x and delta y
    dx = x2 - x1
    dy = y2 - y1

    # Determine the number of steps, which is the maximum of the absolute differences in x or y
    steps = max(abs(dx), abs(dy))
    
    # Calculate the increments in x and y
    Xinc = dx / steps
    Yinc = dy / steps

    # Set the starting points
    x, y = x1, y1
    # Set the pixels along the line
    for _ in range(int(steps) + 1):
        # Set a pixel at the rounded (x, y) coordinates
        set_pixel(int(round(x)), int(round(y)))
        # Increment x and y by one step
        x += Xinc
        y += Yinc

    return img

###########################################################################
# THIS SECTION IS USED TO VIEW THE IMAGE.
"""
path = '/Users/dilaraturkalp/Desktop/cmpe362hw/build.jpeg'
image = cv2.imread(path)
height, width, _ = image.shape 
start_point = (0, 0) 
end_point = (width, height) 
image_rgb = draw_line(image, start_point, end_point, [0, 255, 0], 9)

# Show the image
cv2.imshow("Test Image", image_rgb) 
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
