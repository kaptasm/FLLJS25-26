from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission2():
    #sebesség állítás
    bot.settings(555, 555, 555, 555)

    #homok kihúzás
    kieg_motor_2.run_angle(500,-150, wait=False)
    bot.straight(510)
    kieg_motor_2.run_angle(500,150)
    bot.straight(-70)
    kieg_motor_2.run_angle(500,-150, wait=False)

    #sebesség állítás
    bot.settings(385, 385, 385, 385)

    #hajó felemelés0
    bot.straight(190)
    kieg_motor_1.run_angle(200, -180, wait=False)
    bot.drive(100, 0)
    wait(500)
    bot.stop()
    while not kieg_motor_1.done():
        wait(10)
    #kieg_motor_2.run_angle(200, -100, wait=False)
    bot.settings(777, 777, 777, 777)
    bot.straight(-300)

    #navigálás a keleti bázishoz
    bot.turn(-45)
    bot.straight(240)
    bot.turn(45)
    bot.straight(1000)
    #while not bot.straight.done():
    #    wait(10)
    bot.curve(320, 100)
    #bot.turn(45)
    #bot.straight(200)

if __name__ == "__main__":
    mission2()
