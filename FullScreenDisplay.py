import sys
import time
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk
from itertools import cycle
import glob

class App():
    def __init__(self):
        _ = 0

    def showPIL(self, photos, t):
        self.root = tkinter.Tk()
        self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
        self.root.overrideredirect(1)
        self.root.geometry("%dx%d+0+0" % (self.w, self.h))
        self.root.focus_set()
        self.root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        self.canvas = tkinter.Canvas(self.root, width=self.w, height=self.h)
        self.canvas.pack()
        self.canvas.configure(background='black')
        self.photos = photos
        pilImage = Image.open(next(self.photos))
        imgWidth, imgHeight = pilImage.size
        if imgWidth > self.w or imgHeight > self.h:
            ratio = min(self.w / imgWidth, self.h / imgHeight)
            imgWidth = int(imgWidth * ratio)
            imgHeight = int(imgHeight * ratio)
            pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(pilImage)
        self.imagesprite = self.canvas.create_image(self.w/2, self.h/2, image=self.image)
        self.root.after(t, self.slideshow(t))
        self.root.mainloop()

    def quit(self):
        self.root.destroy()
    def slideshow(self,t):
        try:
            pilImage = Image.open(next(self.photos))
            imgWidth, imgHeight = pilImage.size
            if imgWidth > self.w or imgHeight > self.h:
                ratio = min(self.w / imgWidth, self.h / imgHeight)
                imgWidth = int(imgWidth * ratio)
                imgHeight = int(imgHeight * ratio)
                pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)
            Update_image = ImageTk.PhotoImage(pilImage)
            self.imagesprite = self.canvas.itemconfig(self.image, image=Update_image)
            self.image = Update_image
            self.root.after(t, self.slideshow(t))
        except:
            print("end of iterators")
            # self.root.destroy()

    # def slideShow(self):
    #     pilImage = Image.open(next(self.photos))
    #     imgWidth, imgHeight = pilImage.size
    #     if imgWidth > self.w or imgHeight > self.h:
    #         ratio = min(self.w / imgWidth, self.h / imgHeight)
    #         imgWidth = int(imgWidth * ratio)
    #         imgHeight = int(imgHeight * ratio)
    #         pilImage = pilImage.resize((imgWidth, imgHeight), Image.ANTIALIAS)
    #     image = ImageTk.PhotoImage(pilImage)
    #     imagesprite = self.canvas.config(image=image)
    #     self.root.after(1, self.slideShow)

t = 2000
app = App()
path = 'C:/Users/cheng sun/BoyuanSun/CLIP1&2&etc/*.tif'
img_file_list = glob.glob(path)
print(img_file_list)
photos = iter(_ for _ in img_file_list)
app.showPIL(photos, t)



