from js_base import kieg_motor_1, kieg_motor_2, bot, Stop

def mission6():
    bot.settings(777,777,777,777)
    bot.straight(666)
    bot.turn(32.4)
    bot.settings(333,333,333,333)
    bot.straight(367)
    bot.settings(222,222,222,222)
    kieg_motor_1.run_time(200, 500)
    bot.turn(10)
    kieg_motor_1.run_time(200, 500)
    bot.straight(111)
    bot.straight(-240)
    

if __name__ == "__main__":
    mission6()