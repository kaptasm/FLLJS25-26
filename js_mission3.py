from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission3():
    a = 0
    bot.settings(222, 222, 222, 222)
    bot.straight(616)
    while a !=17:
        kieg_motor_2.run_angle(486, -79)
        kieg_motor_2.run_angle(486, 79)
        a+=1
    bot.straight(-11)
    bot.turn(7)
    bot.straight(44)
    bot.turn(-17)
    bot.straight(-616)
    
    '''#sebesség állítás
    bot.settings(555, 555, 555, 555)

        #homok kihúzás
    kieg_motor_2.run_angle(500,-150, wait=False)
    bot.straight(520)
    kieg_motor_2.run_angle(500,150)
    bot.straight(-70)
    kieg_motor_2.run_angle(500,-150, wait=False)

        #sebesség állítás
    bot.settings(385, 385, 385, 385)

        #hajó felemelés
    bot.straight(190)
    kieg_motor_1.run_angle(200, -180)
    kieg_motor_1.run_angle(200, 150.5)
    bot.settings(777, 777, 777, 777)
    bot.straight(-100)
    bot.straight(100)
    bot.straight(-100)
    bot.straight(100)
    bot.straight(-100)
    bot.straight(100)'''
    '''bot.drive(100, 0)
    wait(500)
    bot.stop()
    while not kieg_motor_1.done():
            wait(10)
        #kieg_motor_2.run_angle(200, -100, wait=False)'''

    '''bot.straight(-300)

        #navigálás a keleti bázishoz
    bot.turn(-45)
    bot.straight(250)
    bot.turn(45)
    bot.straight(1300)
    bot.curve(320, 100)
        #bot.turn(45)
        #bot.straight(200)'''

if __name__ == "__main__":
    mission3()