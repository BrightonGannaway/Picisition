#!/usr/bin/python3

import sys
import os

ys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
sys.path.append("/home/nvidia/.local/lib/python3.10/site-packages/")

from src.constants import Constants


from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput

cap = cv2.VideoCapture(0)


while True:
    count = 0
    ret, frame = cap.read()
    if not ret:
        break

    # Display the resulting frame
    cv2.imshow('frame', frame)

    key = cv2.waitKey(1) & 0xFF

    #test key
    if key == ord('t'):
        print("test key pressed")

    # Press 'q' to exit the loop
    if key == ord('q'):
        break

    # space bar captures image
    if key == ord(' '):
        cv2.imwrite(f"image_game/tests/images/result_{count}.jpg", frame)

print("got here")