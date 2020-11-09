import tkinter as tk
from tb6600 import stepper
from read import read
import time

class Application(tk.Frame):
    def __init__(self, master=None, path = "", pin= [0,0,0]):
        super().__init__(master)
        self.master = master
        self.pack()
        self.power, self.layer, self.time = read(path)
        self.create_widgets()
        self.pin = pin


    def create_widgets(self):
        self.title = tk.Label(self, text="Motor control interface v0")
        self.name = tk.Label(self, text="by Boyuan Sun")
        self.title.pack(side = "top")
        self.name.pack(side = "top")

        self.time_up = tk.Button(self)
        self.time_up["text"] = "time up"
        self.time_up["command"] = self.time_up_f
        self.time_up.pack(side = "top")
        self.time_down = tk.Button(self)
        self.time_down["text"] = "time down"
        self.time_down["command"] = self.time_down_f
        self.time_down.pack(side="top")
        self.time_label = tk.StringVar()
        self.time_label.set("Exposure Time {}".format(self.time))
        self.entrythingy = tk.Entry()
        self.entrythingy.pack()
        self.entrythingy["textvariable"] = self.time_label
        # self.entrythingy.bind('<Key-Return>',self.print_contents)

        self.layer_up = tk.Button(self)
        self.layer_down = tk.Button(self)
        self.layer_up["text"] = "more layer thickness"
        self.layer_down["text"] = "less layer thickness"
        self.layer_up["command"] = self.layer_up_f
        self.layer_down["command"] = self.layer_down_f
        self.layer_up.pack(side="top")
        self.layer_down.pack(side="top")
        self.layer_label = tk.StringVar()
        self.layer_label.set("Layer Thickness {}".format(self.layer))
        self.entrythingy2 = tk.Entry()
        self.entrythingy2.pack()
        self.entrythingy2["textvariable"] = self.layer_label
        # self.entrythingy2.bind('<Key-Return>',self.print_contents2)

        self.speed_label = tk.StringVar()
        self.speed_label.set("Speed (mm/s) {}".format(self.layer/self.time))
        self.entrythingy2 = tk.Entry()
        self.entrythingy2.pack()
        self.entrythingy2["textvariable"] = self.speed_label

        self.run = tk.Button(self)
        self.run["text"] = "Run fab"
        self.run["command"] = self.run_main
        self.run.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def time_up_f(self):
        self.time += 0.025
        self.time_label.set("Exposure Time {}".format(self.time))
        self.speed_label.set("Speed (mm/s) {}".format(self.layer / self.time))
    #
    def time_down_f(self):
        self.time -= 0.025
        self.time_label.set("Exposure Time {}".format(self.time))
        self.speed_label.set("Speed (mm/s) {}".format(self.layer / self.time))
    #
    def layer_up_f(self):
        self.layer += 0.001
        self.layer_label.set("Layer Thickness {}".format(self.layer))
        self.speed_label.set("Speed (mm/s) {}".format(self.layer / self.time))
    #
    def layer_down_f(self):
        self.layer -= 0.001
        self.layer_label.set("Layer Thickness {}".format(self.layer))
        self.speed_label.set("Speed (mm/s) {}".format(self.layer / self.time))

    def run_main(self):
        #hyperparameters
        regular_speed = 8.3
        vertical_range = 110
        layer_n = 3000
        motor_stepsize = 3200
        stepsize = motor_stepsize*self.layer/vertical_range*layer_n
        
        run = stepper(self.pin)
        if self.time:
            fab_speed = self.layer / self.time
        else:
            raise Exception("Time& layer thickness must be positive value")
        print("start")
        for i in range(55):
            run.step(int(stepsize), "right", speed = fab_speed/regular_speed)
        time.sleep(5)
        print("resetting")
        for i in range(55):
            run.step(int(stepsize), "left", speed = 3)
        print("all done")
        run.cleanGPIO()

pins = [17, 27, 22]
path = "input"
root = tk.Tk()
app = Application(master=root, path = path, pin = pins)
app.master.title("Control Interface")
app.master.maxsize(800, 500)
app.mainloop()