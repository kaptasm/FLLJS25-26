from pybricks.tools import hub_menu

from js_base import bot, kieg_motor_1, kieg_motor_2, hub
from js_mission1 import mission1
from js_mission2 import mission2
from js_mission3 import mission3
from js_mission4 import mission4
from js_mission5 import mission5
from js_mission6 import mission6

# Menü, ami összefogja a nyolc küldetésünket
def menu():
    selected = "0"

    while True:

        if selected == "0":
            hub.speaker.beep()
            selected = hub_menu("1", "2", "3", "4", "5", "6", "7")

        elif selected == "1":
            mission1()
            hub.speaker.beep()
            selected = hub_menu("2", "3", "4", "5", "6", "7", "1")

        elif selected == "2":
            mission2()
            hub.speaker.beep()
            selected = hub_menu("3", "4", "5", "6", "7", "1", "2")

        elif selected == "3":
            mission3()
            hub.speaker.beep()
            selected = hub_menu("4", "5", "6", "7", "1", "2", "3")
    
        elif selected == "4":
            mission4()
            hub.speaker.beep()
            selected = hub_menu("5", "6", "7", "1", "2", "3", "4")

        elif selected == "5":
            mission5()
            hub.speaker.beep()
            selected = hub_menu("6", "7", "1", "2", "3", "4", "5")

        elif selected == "6":
            mission6()
            hub.speaker.beep()
            selected = hub_menu("7", "1", "2", "3", "4", "5", "6")

        elif selected == "7":
            mission7()
            hub.speaker.beep()
            selected = hub_menu("1", "2", "3", "4", "5", "6", "7")

menu()