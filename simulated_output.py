# import board
# from adafruit_motor import stepper
# from adafruit_motorkit import MotorKit

# kit = MotorKit(i2c=board.I2C())
#
# kit.stepper1.release()
import time

def single():
    while True:
        print("Single coil steps")
    # for i in range(100):
    #     kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
    # for i in range(100):
    #     kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.SINGLE)
def double():
    while True:
        print("Double coil steps")
    # for i in range(10 0):
    #     kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
    # for i in range(100):
    #     kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
    #
    # print("Interleaved coil steps")
    # for i in range(100):
    #     kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.INTERLEAVE)
    # for i in range(100):
    #     kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.INTERLEAVE)
    #
    # print("Microsteps")
    # for i in range(100):
    #     kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.MICROSTEP)
    # for i in range(100):
    #     kit.stepper1.onestep(direction=stepper.BACKWARD, style=stepper.MICROSTEP)


class Clip():
    def __init__(self, motor_speed = 10):
        """
        Initialization of linear stage
        Arguments:
            speed: the motor speed rmp
            mode:
        """
        self.motor_speed = motor_speed

    def init(self):
        print("set speed to 10")
        print("initialing")
        time.sleep(8)
        print("Done")

    def fab(self, time = 30, layer = 100):
        if time:
            speed = layer/time
            print("speed is {}".format(speed))
        else:
            Exception("Exposure time or layer thickness is not valid!")

        for _ in range(100):
            time.sleep(1/self.motor_speed)
        print("Fabrication")

