from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop, Color, sensor

def mission6():
    bot.use_gyro(False)

    bot.settings(303, 303, 303, 303)

    bot.straight(430)
    kieg_motor_2.run_angle(777, 520)
    bot.straight(-11)
    bot.turn(33.33)
    bot.settings(777, 777, 777, 777)
    bot.straight(333)
    bot.turn(-22)
    #bot.turn(-22.5)
    bot.straight(404)
    bot.straight(-145)
    bot.turn(-36.9)

    bot.use_gyro(False)
    
if __name__ == "__main__":
    mission6()