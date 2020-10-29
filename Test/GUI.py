



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
import tkinter as tk
def _paint(event):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill="red")
    img =  ImageTk.PhotoImage(image=Image.fromarray(data), master=root)
    w.create_image(0, 0, anchor="nw", image=img)
    #w.create_rectangle(50, 25, 150, 75, fill="blue")
    w.update()

def _click(event):
    
    lab["text"] = "clecked"
    x1 =  (event.x - 1)
    print("clecked")
    lab.update()

root = tk.Tk()
w = tk.Canvas(root, width=400, height=400, background="white")
w.pack()
w.bind("<B1-Motion>", _paint)

lab = tk.Label(root, text="status")
lab.pack()

btn = tk.Button(root, text="click me")
btn.pack()
btn.bind("<B1-Motion>", _click)


data = np.zeros((100,100))
tk.mainloop()
