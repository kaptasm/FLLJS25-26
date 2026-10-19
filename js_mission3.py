from js_alap import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission3():
    bot.use_gyro(True)

    bot.settings(700, 700, 700, 700)
    kieg_motor_1.run_time(777, 800, wait=False)
    bot.straight(-820)
    bot.turn(75)
    bot.straight(-21.8)
    #Gyökér megoldása
    kieg_motor_2.run_time(-3000, 1000)
    bot.turn(-75.7)
    bot.settings(500, 500, 500, 500)
    kieg_motor_1.run_time(-777, 766.6, wait=False)
    bot.straight(210)
    bot.turn(-49)
    #Levél megoldása
    kieg_motor_1.run_angle(500, 45)
    bot.straight(-138)
    kieg_motor_1.run_angle(525, 200)
    bot.straight(240)
    bot.settings(600, 600, 600, 600)
    #Vissza navigálás
    bot.turn(-92.7)
    bot.settings(777, 777, 777, 777)
    bot.straight(-600)

    bot.use_gyro(False)


if __name__ == "__main__":
    mission3()
