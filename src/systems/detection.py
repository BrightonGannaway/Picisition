#!/usr/bin/python3

import sys
import os
import argparse
import numpy as np


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Add Jetson Inference Python bindings to PYTHONPATH if not already present
from src.constants import Constants

from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, cudaDeviceSynchronize, cudaFromNumpy, loadImage, saveImage

class Detection:

    def __init__(self):
        self.argv = Constants.DetectNet.argv
        self.input = None
        self.output = None
        self.recent_detections = []

    def detect_object (self, input, output = "db/images/result_out.jpg", network_arg="ssd-mobilenet-v2", overlay="box,labels,conf", threshold_arg=0.5):
        self.net = detectNet(network_arg, argv=self.argv, threshold = threshold_arg)
        
        # cudaDeviceSynchronize()
        # self.input = videoSource(input)
        # #self.input = cudaFromNumpy(self.input)
        # self.output = videoOutput(output)
        # img = self.input.Capture()
        # detections = self.net.Detect(img)

        img = None
        #image input is from a file
        if os.path.isfile(input):
            img = loadImage(input)
            
        if isinstance(input, np.ndarray):
            img = cudaFromNumpy(input)

        if img is None:
            raise ValueError(f"Input image is not valid. Please provide a valid image file or numpy array. Input: {input}")
        
        detections = self.net.Detect(img)
        self.recent_detections = detections
        saveImage(output, img)

        print("detected {:d} objects in image".format(len(detections)))
        for detection in detections:
            print(detection)

        # self.output.Render(img)

        # self.output.SetStatus("{:s} | Network {:.0f} FPS".format(network_arg, self.net.GetNetworkFPS()))
        # print out performance info
        self.net.PrintProfilerTimes()

    # For the game, to pick a clear object as the main focus we detect the most prominent detection using each detection's area and confidence.
    # This is a simple heuristic and can be adjusted based on the specific requirements of the game.
    def get_Most_Prominent_Detection(self):
        if not self.recent_detections:
            print("No recent detections found.")
            return None
        
        if len(self.recent_detections) == 1:
            return self.recent_detections[0]
        
        # Assuming the most prominent detection is the one with the highest area 
        #test if area is returned 
        for detection in self.recent_detections:
            print(f"Detection Area: {detection.Area}")
            
        most_prominent = max(self.recent_detections, key=lambda d: d.Area)
        return most_prominent
    
    def get_detection_class(self, detection):
        if detection is None:
            return None
        if hasattr(detection, 'ClassID'):
            return self.net.GetClassDesc(detection.ClassID)
        
    def get_recent_detections(self):
        return self.recent_detections
    

        

        

        

        
