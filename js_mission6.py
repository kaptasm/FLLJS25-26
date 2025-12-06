from js_base import kieg_motor_1, kieg_motor_2, bot, Stop

def mission6():
    bot.settings(777,777,777,777)
    bot.straight(666)
    bot.turn(29.5)
    bot.settings(333,333,333,333)
    bot.straight(367)
    #bot.turn(8)
    kieg_motor_1.run_time(200, 300)
    bot.turn(24)
    bot.straight(111)
    bot.straight(-240)
    

if __name__ == "__main__":
    mission6()