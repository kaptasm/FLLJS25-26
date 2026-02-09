from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

kieg_motor_1 = Motor(Port.A)
kieg_motor_2 = Motor(Port.E)
nav_motor_1 = Motor(Port.B)
nav_motor_2 = Motor(Port.F, Direction.COUNTERCLOCKWISE)
sensor = ColorSensor(Port.D)
bot = DriveBase(nav_motor_2, nav_motor_1, 55, 105)