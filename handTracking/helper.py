import cv2
from mediapipe import Image, ImageFormat

def cleaning(frame):
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    rgb_frame = Image(image_format=ImageFormat.SRGB, data=rgb)

    return frame, rgb_frame
