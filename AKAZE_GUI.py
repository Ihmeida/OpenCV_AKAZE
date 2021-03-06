
#%%
#https://pythonbasics.org/tkinter-filedialog/
#https://sites.google.com/site/csjhmaker/q-python-xiang-guan/1-tkinter-gui-tu-xing-jie-mian

#%%
import cv2
from PIL import ImageTk 
from PIL import Image  
import tkinter as tk
from tkinter import filedialog as fd 
import os
from datetime import datetime

#%%
def kaze_match(im1_path, im2_path, number:int=20, isShow:bool=False):
    # load the image and convert it to grayscale
    im1 = cv2.imread(im1_path)
    im2 = cv2.imread(im2_path)
    gray1 = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(im2, cv2.COLOR_BGR2GRAY)    

    # initialize the AKAZE descriptor, then detect keypoints and extract
    # local invariant descriptors from the image
    detector = cv2.AKAZE_create()
    (kps1, descs1) = detector.detectAndCompute(gray1, None)
    (kps2, descs2) = detector.detectAndCompute(gray2, None)

    print("keypoints: {}, descriptors: {}".format(len(kps1), descs1.shape))
    print("keypoints: {}, descriptors: {}".format(len(kps2), descs2.shape))    

    # Match the features
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    matches = bf.knnMatch(descs1,descs2, k=2)    # typo fixed

    # Apply ratio test
    good = []
    for m,n in matches:
        if m.distance < 0.9*n.distance:
            good.append([m])

    # cv2.drawMatchesKnn expects list of lists as matches.
    data = cv2.drawMatchesKnn(im1, kps1, im2, kps2, good[0:number], None, flags=2)

    return data

#%%
def AkazeClick(event):
    global canvas
    global img
    if not os.path.isfile(image1):
        info.set("Please read image1")
        return
    elif not os.path.isfile(image2):
        info.set("Please read image2")
        return

    data = kaze_match(image1, image2, isShow=False)
    #fileName = "AKAZE_"+ datetime.now().strftime('%Y-%m-%d_%H_%M_%S') + ".bmp"
    #fileName = os.path.join(os.path.abspath("./"), fileName)
    if(False):
        pass
        #info.set("compare: \n{0} \n{1} \nSave:{2}".format(image1, image2, fileName))
        #Image.fromarray(data).save(fileName)
        #label.update()
    else:
        info.set("compare: \n{0} \n{1}".format(image1, image2))
    img =  ImageTk.PhotoImage(image=Image.fromarray(data), master=root)

    canvas.create_image(0, 0, anchor="nw", image=img)
    canvas.update() 

def CallFile1():
    global image1
    image1= fd.askopenfilename() 
    info.set("Read: {}".format(image1))

def CallFile2():
    global image2
    image2= fd.askopenfilename() 
    info.set("Read: {}".format(image2))

#%%
image1 = ""
image2 = ""
im3 = ""
img = ""

root = tk.Tk()
root.title("RAD AKAZE")
root.geometry("900x800")
info = tk.StringVar()
info.set("Please read image!")

btnCallFile1 = tk.Button(root, text="Read image1", command=CallFile1)
btnCallFile1.pack()

btnCallFile2 = tk.Button(root, text="Read image2", command=CallFile2)
btnCallFile2.pack()

btn = tk.Button(root, text="AKAZE click")
btn.pack()
btn.bind("<Button-1>", AkazeClick)

label = tk.Label(root, textvariable=info, bg="light green")
label.pack()

canvas = tk.Canvas(root, width=900, height=700,  background="white")
canvas.pack()

root.mainloop()
