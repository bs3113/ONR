import tkinter as tk


class Application(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title("Slideshow")
        self.overrideredirect(1)
        self.w, self.h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (self.w, self.h))
        self.resizable(width=False, height=False)
        self.focus_set()
        self.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
        self.current_slide = tk.Label(self)
        self.current_slide.pack()
        self.duration_ms = 100

    def set_image_directory(self, path):
        from pathlib import Path
        from PIL import Image, ImageTk
        from itertools import cycle

        image_paths = Path(path).glob("*.png")
        self.images = cycle(zip(map(lambda p: p.name, image_paths), map(ImageTk.PhotoImage, map(Image.open, image_paths))))

    def display_next_slide(self):
        name, self.next_image = next(self.images)
        self.current_slide.configure(image=self.next_image)
        self.title(name)
        self.after(self.duration_ms, self.display_next_slide)

    def start(self):
        self.display_next_slide()

def main():
    application = Application()
    application.set_image_directory("C:/Users/cheng sun/BoyuanSun/CLIP1&2&etc/Slicing/2/")
    application.start()
    application.mainloop()


if __name__ == "__main__":
    import sys
    sys.exit(main())