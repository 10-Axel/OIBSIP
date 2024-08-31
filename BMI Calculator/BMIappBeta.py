# -*- coding: utf-8 -*-
"""
Created on Aug 24 2024

@author: TIKENDRA
"""
from tkinter import *
from tkinter import messagebox

def on_enter(event):
    event.widget.tk_focusNext().focus_set()

def get_height():
    '''
       This function gets height value from Entry field
    '''
    height = float(ENTRY2.get())
    return height


def get_weight():
    '''
       This function gets weight value from Entry field
    '''
    weight = float(ENTRY1.get())
    return weight


def calculate_bmi(a=""):   # "a" is there because the bind function gives an argument to the function....
    print(a)
    '''
      This function calculates the result
    '''
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = weight / (height ** 2)
    except ZeroDivisionError:
        messagebox.showinfo("Result", "Please enter positive height!!")
    except ValueError:
        messagebox.showinfo("Result", "Please enter valid data!")
    else:
        if bmi <= 15.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You are Very severely underweight!!"
            messagebox.showinfo("Result", res)
        elif 15.0 < bmi <= 16.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You are Severely underweight!"
            messagebox.showinfo("Result", res)
        elif 16.0 < bmi < 18.5:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You are Underweight!"
            messagebox.showinfo("Result", res)
        elif 18.5 <= bmi <= 25.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You are Normal."
            messagebox.showinfo("Result", res)
        elif 25.0 < bmi <= 30:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You are Overweight."
            messagebox.showinfo("Result", res)
        elif 30.0 < bmi <= 35.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You are Moderately obese!"
            messagebox.showinfo("Result", res)
        elif 35.0 < bmi <= 40.0:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You are Severely obese!"
            messagebox.showinfo("Result", res)
        else:
            res = "Your BMI is " + str(bmi) + "\nRemarks: You are Super obese!!"
            messagebox.showinfo("Result", res)


if __name__ == '__main__':
    TOP = Tk()
    #TOP.bind("<Return>", calculate_bmi)
    TOP.geometry("500x430")
    TOP.configure(background="#1DA2CA")
    TOP.title("BMI Calculator")
    TOP.resizable(width=False, height=False)
    LABLE = Label(TOP, bg="#1DA2CA", text="Welcome to BMI Calculator", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=120, y=20)
    LABLE1 = Label(TOP, bg="#cef0f1", text="Enter Weight (in kg):", bd=3,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=115, y=110)
    ENTRY1 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY1.place(x=320, y=110)
    ENTRY1.focus_set()
    ENTRY1.bind("<Return>", lambda event: ENTRY2.focus_set())
    LABLE2 = Label(TOP, bg="#cef0f1", text="Enter Height (in cm):", bd=3,
                   font=("Helvetica", 10, "bold"), pady=5)
    LABLE2.place(x=115, y=171)
    ENTRY2 = Entry(TOP, bd=8, width=6, font="Roboto 11")
    ENTRY2.place(x=320, y=171)
    ENTRY2.bind("<Return>", lambda event: BUTTON.focus_set())
    BUTTON = Button(bg="#FC0B13", bd=8, text="BMI", padx=33, pady=12, command=calculate_bmi,
                    font=("Helvetica", 16, "bold"))
    BUTTON.grid(row=3, column=0, sticky=W)
    BUTTON.place(x=180, y=270)
    BUTTON.bind("<Return>", calculate_bmi)
    TOP.mainloop()

    