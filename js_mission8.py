from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop, Color, sensor

def mission8():
    bot.use_gyro(False)

    bot.settings(303, 303, 303, 303)

    bot.straight(555.5)
    kieg_motor_2.run_angle(777, 482)
    bot.straight(-11)
    bot.turn(33.33)
    bot.settings(777, 777, 777, 777)
    bot.straight(333)
    bot.turn(-12.3)
    bot.straight(404)
    bot.straight(-202)

    bot.use_gyro(False)
    
if __name__ == "__main__":
    mission8()