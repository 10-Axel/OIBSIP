# -*- coding: utf-8 -*-
"""
Created on Aug 21 2024 

@author: TIKENDRA
"""

import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import os
import sys

engine = pyttsx3.init('sapi5')

def speak(audio) :
    engine.say(audio)
    #print(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good Morning Sir")
    elif hour>12 and hour<=18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    
    strTime = datetime.datetime.now()  
    #current_time = datetime.now()
    formatted_date = strTime.strftime("%d %B %Y , %A.")
    speak(f"Today is {formatted_date}")
    formatted_time = strTime.strftime("%I:%M %p")
    speak(f"And It's {formatted_time}")
    
    speak("I am Vaassi, Your Virtual Guide for The BMI Calculation")

def calculate_bmi(weight, height):   #Calculate the BMI (Body Mass Index) using weight in kilograms and height in centimeters. Formula: BMI = weight (kg) / ((height (cm) * height (cm))/100^2)
    bmi = (weight*(100**2)) / (height ** 2)
    return bmi

def result(bmi):   #Interpret the BMI value and return the corresponding category.
    if bmi < 18.5:
        return "Underweight. Please take the appointment from your healthcare"
    elif bmi >= 18.5 and bmi < 25:
        return "Normal weight"
    elif bmi >= 25 and bmi < 30:
        return "Overweight"
    else:
        return "Obese. Please take the appointment from your healthcare"
    
def main():
    speak("Enter your weight in Kilograms Sir")
    weight = float(input("Enter your weight in kilograms: "))
    speak("Enter your height in Centimeters Sir")
    height = float(input("Enter your height in centimeters: "))

    bmi = calculate_bmi(weight, height)
    category = result(bmi)

    print(f"Your BMI is {bmi:.2f}, which is {category}.")
    speak(f"Your BMI is {bmi:.2f}, which is {category}.")
    
    print("Drink atleast 3 litres of water per day and do exercise on the regular basis.")
    speak("Drink atleast 3 litres of water per day and do exercise on the regular basis.")

if __name__ == "__main__":
    clear = lambda: os.system('cls')
    clear()
    wish()
    main()
    speak("Thanks for using me sir, have a good day.")
    sys.exit()