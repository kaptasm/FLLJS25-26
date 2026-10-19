from js_alap import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop


def mission1():

    bot.use_gyro(True)

    #Futam 1

    #Zászló ledöntés
    kieg_motor_1.run_time(777, 800, wait=False)
    kieg_motor_2.run_time(-777, 800, wait=False)
    bot.settings(777, 777, 777, 777)
    bot.straight(-350)
    bot.straight(50)
    kieg_motor_1.run_time(-777, 800, wait=False)
    kieg_motor_2.run_time(777, 800, wait=False)
    bot.straight(400)

    bot.use_gyro(False)

if __name__ == "__main__":
    mission1()
