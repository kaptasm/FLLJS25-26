from js_base import kieg_motor_1, kieg_motor_2, bot, Stop

def mission5():
    bot.settings(777,777,777,777)
    bot.straight(666)
    bot.turn(30)
    bot.settings(333,333,333,333)
    bot.straight(369)
    kieg_motor_1.run_time(200, 500)
    bot.turn(10)
    bot.straight(111)
    bot.straight(-240)

if __name__ == "__main__":
    mission5()