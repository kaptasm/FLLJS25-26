from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission4():
    bot.settings(777,777,777,777)
    bot.straight(350)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(888,800)
    bot.straight(-350)


if __name__ == "__main__":
    mission4()