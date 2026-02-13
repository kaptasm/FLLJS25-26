from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop, Color, sensor

def mission7():
    bot.use_gyro(True)
    bot.settings(777,777,777,777)
    bot.straight(840, Stop.NONE)
    bot.turn(22)
    bot.straight(400)
    bot.straight(-250)

    '''kesz = False
    menetszam = 0

    kieg_motor_2.run_angle(248, 39)
    bot.straight(800)
    while not kesz:
        if sensor.color() == Color.WHITE or menetszam>=7:
            bot.turn(57)
            kesz = True
        else:
            bot.straight(23.4)
            menetszam += 1
    bot.straight(234)'''
    '''  kieg_motor_2.run_angle(777, -39)
    kieg_motor_2.run_angle(777, 33)'''

    '''kieg_motor_2.run_angle(100,-90,wait=False)
    bot.settings(777,777,777,777)
    bot.straight(666)
    bot.turn(30)
    bot.settings(333,333,333,333)
    bot.straight(360)
    kieg_motor_1.run_time(30, 500)
    #bot.settings(777,777,777,777)
    ##bot.turn(-7)
    #bot.turn(10)
    #kieg_motor_1.run_time(40, 500)
    #bot.turn(-15)
    #kieg_motor_1.run_time(50, 500)
    #bot.straight(111)
    #kieg_motor_2.run_time(60, 500,)
    #bot.turn(-10)
    #bot.straight(-240)

    bot.turn(-15)
    bot.straight(550)
    bot.turn(-20)
    bot.straight(270)'''

    bot.use_gyro(False)
    

if __name__ == "__main__":
    mission7()