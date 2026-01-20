from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission2():
    bot.settings(777, 777, 777, 777)
    bot.straight(575)
    bot.turn(7.7)
    bot.straight(-100)
    bot.turn(-16)
    bot.straight(200)
    bot.straight(-178)
    bot.straight(144)
    kieg_motor_2.run_angle(222, -45)
    bot.straight(155)
    kieg_motor_2.run_angle(222, -189)
    bot.straight(-399)
    bot.turn(30)
    bot.straight(-400)
if __name__ == "__main__":
    mission2()