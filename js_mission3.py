from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop, Color, sensor

def mission3():
    bot.use_gyro(False)

    bot.settings(777,777,777,777)
    bot.straight(444)
    bot.straight(-555)

    bot.use_gyro(False)
    
if __name__ == "__main__":
    mission3()