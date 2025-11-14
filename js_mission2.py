from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission2():
    #sebesség állítás
    bot.settings(555, 555, 555, 555)

    #homok kihúzás
    kieg_motor_2.run_angle(200,-200)
    bot.straight(515)
    kieg_motor_2.run_angle(200,200)
    bot.straight(-70)
    kieg_motor_2.run_angle(200,-200)

    #sebesség állítás
    bot.settings(385, 385, 385, 385)

    #hajó felemelés
    bot.straight(250)
    kieg_motor_2.run_angle(200, -100)
    kieg_motor_1.run_angle(200, -180)
    bot.settings(777, 777, 777, 777)
    bot.straight(-300)

    #navigálás a keleti bázishoz
    bot.turn(-45)
    bot.straight(155)
    bot.turn(40)
    bot.straight(1100)
    bot.turn(45)
    bot.straight(180)

if __name__ == "__main__":
    mission2()
