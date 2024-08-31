# -*- coding: utf-8 -*-
"""
Created on Aug 22 2024

@author: TIKENDRA
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class BMI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("BMI Calculator")

        # Create labels and entry fields for weight and height
        self.label_weight = tk.Label(self.root, text="Weight (kg):")
        self.label_weight.pack()
        self.entry_weight = tk.Entry(self.root)
        self.entry_weight.pack()

        self.label_height = tk.Label(self.root, text="Height (cm):")
        self.label_height.pack()
        self.entry_height = tk.Entry(self.root)
        self.entry_height.pack()

        # Create a button to calculate BMI
        self.button = tk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.button.pack()

        # Create a label to display the result
        self.label_result = tk.Label(self.root, text="")
        self.label_result.pack()

    def calculate_bmi(self):
        weight = float(self.entry_weight.get())
        height = float(self.entry_height.get())

        # Calculate BMI
        height_in_meters = height / 100
        bmi = weight / (height_in_meters ** 2)

        # Display BMI category
        if bmi <= 16:
            category = "Severe Thinness"
        elif 16 < bmi <= 17:
            category = "Mild Thinness"
        elif 17 < bmi <= 18.5:
            category = "Moderate Thinness"
        elif 18.5 < bmi <= 25:
            category = "Normal"
        elif 25 < bmi <= 30:
            category = "Overweight"
        elif 30 <= bmi <= 35:
            category = "Obese Class I"
        elif 35 <= bmi <= 40:
            category = "Obese Class II"
        elif bmi > 40:
            category = "Obese Class III"

        self.label_result.config(text=f"BMI: {bmi:.2f}, Category: {category}")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = BMI()
    game.run()