from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop, Color, sensor

def mission1():
    bot.use_gyro(True)

    kesz = False
    menetszam = 0

    bot.settings(488, 488, 488, 488)
    #csille, kincs
    bot.straight(974)
    bot.turn(88)
    kieg_motor_1.run_angle(777, -234, wait=False)
    kieg_motor_2.run_angle(777, 234)
    bot.straight(67)

    while not kesz:
        if sensor.color() == Color.WHITE or menetszam>=7:
            bot.straight(56)
            kieg_motor_2.run_angle(111, -63)
            kieg_motor_1.run_time(111, 2340)
            kesz = True
        else:
            bot.straight(23.4)
            menetszam += 1

    kieg_motor_1.run_time(-111, 2340)
    bot.settings(234, 234, 234, 234)
    bot.straight(-167)
    bot.settings(777,777,777,777)
    kieg_motor_2.run_angle(777, -67)
    bot.turn(39)
    bot.straight(389)
    bot.turn(-7)
    kieg_motor_1.run_time(777, 336)
    bot.turn(-24)
    bot.straight(-444)
    bot.turn(22)
    bot.straight(-99)
    bot.straight(67)
    bot.turn(16.7)
    bot.straight(-99)
    bot.curve(488, 180)

    bot.use_gyro(False)
    
if __name__ == "__main__":
    mission1()