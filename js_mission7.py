from js_base import kieg_motor_1, kieg_motor_2, bot, Stop

def mission7():
    kieg_motor_2.run_angle(100,-90,wait=False)
    bot.settings(777,777,777,777)
    bot.straight(666)
    bot.turn(35)
    bot.settings(333,333,333,333)
    bot.straight(367)
    bot.settings(222,222,222,222)
    #bot.turn(4)
    bot.settings(777,777,777,777)
    kieg_motor_1.run_time(200, 500)
    bot.turn(5)
    kieg_motor_1.run_time(200, 500)
    bot.turn(5)
    kieg_motor_1.run_time(200, 700)
    bot.straight(111)
    kieg_motor_2.run_time(200, 500,)
    bot.turn(-10)
    bot.straight(-240)
    

if __name__ == "__main__":
    mission7()