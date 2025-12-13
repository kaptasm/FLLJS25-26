from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission1():

    bot.settings(222, 222, 222, 222)
    bot.straight(-69)
    bot.turn(44)
    bot.straight(-139)
    bot.turn(-44)
    bot.straight(-595)
    bot.turn(-91)

    bot.settings(111, 111, 111, 111)
    bot.straight(199)
    kieg_motor_1.run_angle(111, 303)
    kieg_motor_2.run_angle(111, -52)
    bot.turn(-3.9)
    bot.straight(-108)
    bot.turn(97)
    kieg_motor_2.run_angle(111, -55)
    
    bot.settings(777, 777, 777, 777)
    bot.straight(155)
    bot.turn(20)
    bot.settings(370,370,370,370)
    bot.straight(400)
    bot.settings(777, 777, 777, 777)
    bot.straight(-300)
    bot.turn(-76)
    bot.straight(-100)
    bot.turn(15)
    bot.straight(-90)
    bot.turn(-16)
    bot.straight(170)
    bot.turn(-40)
    bot.straight(120)
    bot.turn(127)
    bot.straight(700)
    
if __name__ == "__main__":
    mission1()
