



#import tkinter as tk
#window = tk.Tk()
#window.title("AKAZE")
#window.geometry("400x400")
#
#label = tk.Label(window, text="AKAZE", bg="green")
#label.pack()
#
#btn = tk.Button(window, text="AKAZE click", command=akazeClick)
#btn.pack()00o
#
#window.mainloop()
x = input()
print(x*100)
y= input()
print(y*100)

import tkinter as tk
window = tk.Tk()
window.title("AKAZE")
window.geometry("400x400")

label = tk.Label(window, text="AKAZE", bg="green")
label.pack()

btn = tk.Button(window, text="AKAZE click")
btn.pack()

window.mainloop()



#%%
from tkinter import *
from PIL import Image, ImageTk


def main():
    root = Tk()
    w = Canvas(root, width=400, height=400, background="white")
    w.pack()

    def _paint(event):
        # event.x 鼠標左鍵的橫坐標
        # event.y 鼠標左鍵的縱坐標
        #x1, y1 = (event.x - 1), (event.y - 1)
        #x2, y2 = (event.x + 1), (event.y + 1)
        #w.create_oval(x1, y1, x2, y2, fill="red")
        #w.create_oval(x1, y1, x2, y2, fill="red")

        im3 = np.zeros((100,100))
        img =  ImageTk.PhotoImage(image=Image.fromarray(im3), master=root)
        w.create_image(0, 0, anchor="nw", image=img)
        w.update()

    # 鼠標左鍵一點，就畫出了一個小的橢圓
    # 畫布與鼠標左鍵進行綁定
    w.bind("<B1-Motion>", _paint)

    mainloop()


if __name__ == "__main__":
    main()

#%%
from tkinter import *
import numpy as np
from PIL import ImageTk 
from PIL import Image  

root = Tk()


#imLabel = tk.Label(root,image=img).pack()
imLabel = tk.Label(root, text="helolo")
imLabel.pack()


#imLabel.config(text="New text")
# or
#imLabel["text"] = "New text"

w = Canvas(root, width=400, height=400, background="white")
w.pack()
def _paint(event):
    global data
    global img

    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill="red")
    
    data = data + 1
    img =  ImageTk.PhotoImage(image=Image.fromarray(data), master=root)
    w.create_image(0, 0, anchor="nw", image=img)
    imLabel["image"] =img
    w.update()

data = np.zeros((100,100))


img =  ImageTk.PhotoImage(image=Image.fromarray(data), master=root)


w.bind("<B1-Motion>", _paint)
mainloop()
