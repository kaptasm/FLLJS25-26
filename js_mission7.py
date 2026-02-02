from js_base import kieg_motor_1, kieg_motor_2, bot, Stop

def mission7():
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
    #bot.straight(-240)'''

    bot.turn(-15)
    bot.straight(550)
    bot.turn(-20)
    bot.straight(270)
    

if __name__ == "__main__":
    mission7()