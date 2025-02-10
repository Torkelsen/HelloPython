import cv2
import numpy as np
from PIL import Image

# TODO: also converting yellow and blue, so the sun become blue and snow become yellow

def remove_white_background(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define white range in HSV (higher V = white)
    lower_white = np.array([0, 0, 240], dtype=np.uint8)
    upper_white = np.array([180, 30, 255], dtype=np.uint8)

    # Create a mask for white pixels
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    # Convert to RGBA and apply transparency
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    image[white_mask > 0] = [0, 0, 0, 0]  # Transparent

    return Image.fromarray(image)

image_names = ['Clear_org', 'Clouds_org', 'Rain_org', 'Snow_org']
for old_name in image_names:
    transparent_image = remove_white_background(f"images/{old_name}.png")
    transparent_image.save(f"images/{old_name.replace('_org', '')}.png")