__author__ = "Axel Aviloff"

from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import numpy as np
from PIL import ImageTk, Image
from cmath import sqrt


def delEntries():
    entry_A.delete(0, END)
    entry_B.delete(0, END)
    entry_C.delete(0, END)


def isNumber(x):
    try:
        float(x)
        return True
    
    except:
        return False


def calculateRoots(A, B, C):
    if A == "0":
        messagebox.showerror("Invalid input", "'A' need to be different from 0")
        delEntries()
    
    elif not(isNumber(A) and isNumber(B) and isNumber(C)):
        messagebox.showerror("Invalid input", "Enter numbers only")
        delEntries()
    
    else:
        newWindow = Tk()
        newWindow.geometry('650x600')
        newWindow.title("Result")
        newWindow.resizable(False, False)
        newWindow['bg'] = "white"
        
        A = float(A)
        B = float(B)
        C = float(C)
        
        delta = B ** 2 - 4 * A * C
        

        if A > 0:
                conca = "UPWARD"
        
        else:
            conca = "DOWNWARD"

        
        if delta >= 0:      
            x1 = (-B + delta ** (1/2))/(2*A)
            x2 = (-B - delta ** (1/2))/(2*A)
        
        else:
            x1 = (-B + sqrt(delta))/(2*A)
            x2 = (-B - sqrt(delta))/(2*A)
            

        lbl_result = Label(newWindow, text = "ROOTS AND DELTA:", bg = "white", font = "bold")
        lbl_delta = Label(newWindow, text = "Δ = {}".format(delta), bg = "white")
        lbl_x1 = Label(newWindow, text = "X' = {}".format(x1), bg = "white")
        lbl_x2 = Label(newWindow, text = "X'' = {}".format(x2), bg = "white")
        lbl_conc = Label(newWindow, text = "Concavity = {}".format(conca), bg = "white")
        lbl_plot = Label(newWindow, text = "PLOT:", bg = "white", font = "bold")
        lbl_result.place(x = 0, y = 0)
        lbl_delta.place(x = 0, y = 20)
        lbl_x1.place(x = 0, y = 40)
        lbl_x2.place(x = 0, y = 60)
        lbl_conc.place(x = 0, y = 80)
        lbl_plot.place(x = 0, y = 100)
        
        x = np.linspace(-10, 10, 1000)
        y = int(A)*(x**2) + int(B)*x + int(C)  

        figure = plt.Figure()
        plt.autoscale()
        ax = figure.add_subplot(1,1,1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        ax.plot(x,y, 'r')
        chart_type = FigureCanvasTkAgg(figure, newWindow)
        chart_type.get_tk_widget().place(x = 4, y = 120)
        
        delEntries()

        newWindow.mainloop

def showResult():
    calculateRoots(entry_A.get(), entry_B.get(), entry_C.get())
    

window = Tk()
window.resizable(False, False)
window.geometry('285x90')
window.title("Bhaskara Calculator")

img = Image.open("01.png")
img = img.resize((70, 70), Image.ANTIALIAS)
panel = ImageTk.PhotoImage(img)

lbl_title = Label(window, text="Enter the values ​​of A, B and C respectively:", fg="black")
lbl_A = Label(window, text = "x²+", fg="red", font=("comic-sans", 12))
lbl_B = Label(window, text = "x+", fg="red", font=("comic-sans", 12))
entry_A = Entry(window,width=4)
entry_B = Entry(window,width=4)
entry_C = Entry(window,width=4)
calculate_btn = Button(text = "Calculate", command = showResult)
lbl_img = Label(window, image = panel)

lbl_title.place(x = 0, y = 0)
entry_A.place(x = 2, y = 20)
lbl_A.place(x = 40, y = 20)
entry_B.place(x = 70, y = 20)
lbl_B.place(x = 110, y = 20)
entry_C.place(x = 135, y = 20)
calculate_btn.place(x = 2, y = 50)
lbl_img.place(x = 190, y = 18)

window.mainloop()