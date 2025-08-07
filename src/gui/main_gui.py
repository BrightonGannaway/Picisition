#!/usr/bin/python3
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import threading
import time


import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.systems.detection import Detection
from src.systems.game_systems.game_runner import Game_Runner

class Main_GUI:
    def __init__(self):

        self.detector = Detection()
        self.runner = Game_Runner()

        self.root = tk.Tk()
        self.root.title("Livestream GUI")

        self.video_label = tk.Label(self.root)
        self.video_label.pack()

        self.analysis_result_label = tk.Label(self.root, text="Analysis Result: ")
        self.analysis_result_label.pack()

        self.cap = cv2.VideoCapture(0)
        self.capture_name = "input"

        self.capture_button = tk.Button(self.root, text="Capture", command=self.capture)
        self.capture_button.pack()

        # self.analyze_button = tk.Button(self.root, text="analyze", command=self.analyze_capture)
        # self.analyze_button.pack()

        self.exit_button = tk.Button(self.root, text="Exit", command=self.close_app)
        self.exit_button.pack()

        #goal check emmitter 

        self.update_video()  # Start the video update loop

        self.root.protocol("WM_DELETE_WINDOW", self.close_app)

    def update_video(self):
        ret, frame = self.cap.read()
        if ret:
            cv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_image = Image.fromarray(cv_image)
            tk_image = ImageTk.PhotoImage(image=pil_image)

            self.video_label.config(image=tk_image)
            self.video_label.image = tk_image

        self.root.after(10, self.update_video)

    def capture(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imwrite(f"db/images/{self.capture_name}.jpg", frame)
            self.analyze_capture(input=frame)

    def analyze_capture(self, input="db/images/{self.capture_name}.jpg"):
        self.detector.detect_object(input=input, output="db/images/result_out.jpg")
        # self.detector.detect_object(f"db/images/{self.capture_name}.jpg", output="db/images/result_out.jpg")

        result_text = self.get_analysis_result()
        self.set_analysis_result(result_text)

    def get_analysis_result(self):
        prominent = self.detector.get_Most_Prominent_Detection()

        if prominent is None:
            return "No objects detected"
        
        class_name = self.detector.get_detection_class(prominent)

        if class_name is None:
            return "No class detected"
        
        value = self.runner.relate_guess_to_goal(class_name)
        if value is None:
            result_str = "\nResult: No relation found - please try again with a different guess"
            return result_str

        result_str = f"Result: {(value * 100):.2f}% related to goal"

        if value == 1.0:
            result_str = "CORRECT - " + result_str
            

        return f"Detected: {class_name}" + "\n" + result_str

    def request_goal_match(self):
        return self.runner

    def set_analysis_result(self, result_text):
        self.analysis_result_label.config(text=result_text)

    def close_app(self):
        self.cap.release()
        self.root.destroy()

    def run(self):
        self.runner.run()
        self.root.mainloop()

# To run the GUI
if __name__ == "__main__":
    Main_GUI()
