
#%%
import tkinter as tk
from PIL import ImageTk 
from PIL import Image  
import numpy as np
data = np.zeros((100,100))

# 藉由 event(mouse) 來觸發事件

# 滑鼠拖曳作畫
def _paint(event):
    global data
    global img
    global w
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    w.create_oval(x1, y1, x2, y2, fill="red")

# 點擊 Canvas 更換 canvas
def CanvasClick(event):
    global data
    global img
    global w2
    data = (data + 10) %255
    print("CanvasClick" + str(data[0,0]))
    img =  ImageTk.PhotoImage(image=Image.fromarray(data), master=root)
    w2.create_image(0, 0, anchor="nw", image=img)

# 點擊 button 更換 label
def btnClick(event):
    global data
    global img

    data = (data + 10) %255
    img =  ImageTk.PhotoImage(image=Image.fromarray(data), master=root)
    print("BtnClick" + str(data[0,0]))

    # 用 label 取代 Canvas, 參數可用 dict 代回去
    lab["image"] = img

root = tk.Tk()
img =  ImageTk.PhotoImage(image=Image.fromarray(data), master=root)

# <Button-1> 1代表左鍵，2代表中鍵，3代表右鍵
# <B1-Motion> 1代表按下左鍵拖動，2代表中鍵，3代表右鍵
w = tk.Canvas(root, width = 100, height=100, background="white")
w.pack()
w.bind("<B1-Motion>", _paint)

w2 = tk.Canvas(root, width=100, height=100)
w2.create_image(0, 0, anchor="nw", image=img)
w2.pack()
w2.bind("<Button-1>", CanvasClick)

# label 文字跟 image 2選1
lab = tk.Label(root, text="status")
lab.pack()

btn = tk.Button(root, text="click me")
btn.pack()
btn.bind("<Button-1>", btnClick)

tk.mainloop()
