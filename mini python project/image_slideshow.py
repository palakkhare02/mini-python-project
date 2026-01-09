from itertools import cycle
from PIL import Image ,ImageTk
import time
import tkinter as tk

# set root window using tkinter
root =tk.Tk()
root.title("Image Slideshow Viewer")

# list of images that show in slideshow
image_path=[
  r"C:\Users\apk14\OneDrive\Pictures\ronak's wedding\1F5A0055.JPG",
  r"C:\Users\apk14\OneDrive\Pictures\ronak's wedding\1F5A0075.JPG",
  r"C:\Users\apk14\OneDrive\Pictures\ronak's wedding\1F5A9593.JPG",
  r"C:\Users\apk14\OneDrive\Pictures\ronak's wedding\DSC08729.JPG",
  r"C:\Users\apk14\OneDrive\Pictures\ronak's wedding\DSC07986.JPG",
  r"C:\Users\apk14\OneDrive\Pictures\ronak's wedding\1F5A0101.JPG",
]
# image resize to 1080*1080 - use open method of image class of pil module 

image_size=(1080,1080)
images=[Image.open(path) .resize(image_size) for path in image_path]

photo_images=[ImageTk.PhotoImage(image) for image in images]

label=tk.Label(root)
label.pack()

def update_image():
  for photo_image in photo_images:
    label.config(image=photo_image)
    label.update()
    time.sleep(2)


slideshow=cycle(photo_images) 

def start_slideshow():
  for _ in range(len(image_path)):
    update_image()

play_buttton=tk.Button(root, text ="play slideshow" ,command=start_slideshow)
play_buttton.pack()    

root.mainloop()

