from js_base import bot, kieg_motor_1, wait

def mission3():
    bot.use_gyro(True)
    ismetles = 0
    bot.settings(555, 555, 555, 555)
    bot.straight(626)
    kieg_motor_1.run_angle(777, -39)
    bot.turn(7)
    bot.straight(-111)
    bot.turn(-46)
    bot.straight(363)
    bot.turn(44)
    bot.straight(166)
    bot.turn(76)
    bot.straight(52)
    bot.turn(-3)
    bot.use_gyro(False)
    while ismetles!=10:
        bot.turn(-28)
        bot.turn(27)
        ismetles+=1
    bot.use_gyro(True)
    bot.turn(-7)
    bot.straight(-69)
    bot.turn(-69)
    bot.straight(730)

if __name__ == "__main__":
    mission3()