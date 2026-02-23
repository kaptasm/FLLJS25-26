from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop, Color, sensor

def mission7():
    bot.use_gyro(False)

    bot.settings(303, 303, 303, 303)

    bot.straight(430)
    kieg_motor_2.run_angle(777, 520)
    bot.straight(-11)
    bot.turn(33.33)
    bot.settings(777, 777, 777, 777)
    bot.straight(333)
    bot.turn(-16)
    bot.straight(404)
    bot.straight(-202)

    bot.use_gyro(False)
    
if __name__ == "__main__":
    mission7()