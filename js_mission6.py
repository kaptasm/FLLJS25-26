from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission6():
    bot.use_gyro(True)
    #Keleti Bázisról elindulás
    bot.settings(777,777,777,777)
    bot.straight(350)
    #siló (08)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(888,800)
    #Bázisra visszatérés
    bot.straight(-350)
    bot.use_gyro(False)


if __name__ == "__main__":
    mission6()