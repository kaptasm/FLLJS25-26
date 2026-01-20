from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop, Color

def mission1():

    a = True
    b = 0

    bot.settings(488, 488, 488, 488)
    #csille, kincs
    bot.straight(963)
    bot.turn(88)
    kieg_motor_1.run_angle(777, -234, wait=False)
    kieg_motor_2.run_angle(777, 234)

    while a:
        if sensor.color() == Color.WHITE or b>=7:
            bot.straight(56)
            kieg_motor_2.run_angle(111, -67)
            kieg_motor_1.run_time(111, 2340)
            a = False
        else:
            bot.straight(23.4)
            b += 1

    kieg_motor_1.run_time(-111, 2340)
    bot.settings(234, 234, 234, 234)
    bot.straight(-167)
    bot.settings(777,777,777,777)
    kieg_motor_2.run_angle(777, -67)
    bot.turn(90)
    bot.straight(288)
    kieg_motor_1.run_time(777, 1370)
    bot.turn(-53)
    bot.straight(-282)
    bot.straight(33.5)
    bot.turn(7.7)
    bot.straight(-67)
    bot.settings(777, 777, 777, 777)
    bot.straight(199)
    bot.turn(56)
    bot.straight(677)
    
if __name__ == "__main__":
    mission1()