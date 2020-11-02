import tkinter as tk
from simulated_output import Clip
from read import read

class Application(tk.Frame):
    def __init__(self, master=None, path = ""):
        super().__init__(master)
        self.master = master
        self.pack()
        self.power, self.thickness, self.time = read(path)
        self.create_widgets()


    def create_widgets(self):
        self.title = tk.Label(self, text="Motor control interface v0")
        self.name = tk.Label(self, text="by Boyuan Sun")

        self.time_up = tk.Button(self)
        self.time_up["text"] = "time up"
        self.time_up["command"] = self.time_up_f
        self.time_up.pack(side = "top")
        self.time_down = tk.Button(self)
        self.time_down["text"] = "time down"
        self.time_down["command"] = self.time_down_f
        self.time_down.pack(side="top")
        self.time_label = tk.StringVar()

        self.layer_up = tk.Button(self)
        self.layer_down = tk.Button(self)
        self.layer_up["text"] = "more layer thickness"
        self.layer_down["text"] = "less layer thickness"
        self.layer_up["command"] = self.layer_up_f
        self.layer_down["command"] = self.layer_down_f
        self.layer_up.pack(side="top")
        self.layer_down.pack(side="top")
        self.layer_label = tk.StringVar()

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def time_up_f(self):
        self.time += 0.025
        self.time_label = tk.Label(self, text="Exposure Time is {} (s)".format(self.time))

    def time_down_f(self):
        self.time -= 0.025
        self.time_label = tk.Label(self, text="Exposure Time is {} (s)".format(self.time))

    def layer_up_f(self):
        self.layer += 0.001
        self.layer_label = tk.Label(self, text="Layer thickness is {} (mm)".format(self.time))

    def layer_down_f(self):
        self.layer -= 0.001
        self.layer_label = tk.Label(self, text="Layer thickness is {} (mm)".format(self.time))


path = "input"
root = tk.Tk()
app = Application(master=root, path = path)
app.mainloop()