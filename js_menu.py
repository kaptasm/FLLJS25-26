from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu

from js_base import bot, kieg_motor_1, kieg_motor_2, hub
from js_mission1 import mission1
from js_mission2régi import mission2
from js_mission3 import mission3
from js_mission4 import mission4
from js_mission55 import mission5
from js_mission6 import mission6


# menu ami osszefogja a het kuldetesunket
def menu():
    selected = "0"
    while True:

        # Based on the selection, run a program.
        if selected == "0":
            hub.speaker.beep()
            selected = hub_menu("1", "2", "3", "4", "5","6")
        elif selected == "1":
            mission1()
            hub.speaker.beep()
            selected = hub_menu("2", "3", "4", "5","6", "1")
        elif selected == "2":
            mission2()
            hub.speaker.beep()
            selected = hub_menu("3", "4", "5","6", "1","2")
        elif selected == "3":
            mission3()
            hub.speaker.beep()
            selected = hub_menu("4", "5","6", "1","2", "3")
        elif selected == "4":
            mission4()
            hub.speaker.beep()
            selected = hub_menu("5","6", "1","2", "3", "4")
        elif selected == "5":
            mission5()
            hub.speaker.beep()
            selected = hub_menu("1", "2", "3", "4", "5","6")
        elif selected == "6":
            mission6()
            hub.speaker.beep()
            selected = hub_menu( "1", "2", "3", "4", "5", "6")
        '''elif selected == "7":
            mission7()
            hub.speaker.beep()
            selected = hub_menu("1", "2", "3", "4", "5", "6", "7")'''
 #abc

menu()
