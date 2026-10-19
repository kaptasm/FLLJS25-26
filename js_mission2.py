from js_alap import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission2():
    bot.use_gyro(True)

    #Futam 3
    bot.turn(51)
    bot.settings(777, 777, 777, 777)
    bot.straight(-460)
    bot.settings(400, 400, 400, 400)
    kieg_motor_2.run_time(-400, 520)
    bot.settings(100, 100, 100, 100)
    bot.straight(120)
    kieg_motor_2.run_time(-100, 150)
    bot.straight(0)
    bot.settings(777, 777, 777, 777)
    bot.straight(350)

    bot.use_gyro(False)

if __name__ == "__main__":
    mission2()
