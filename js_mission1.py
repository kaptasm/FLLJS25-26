from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop, Color, sensor

def mission1():
    bot.use_gyro(True)

    kesz = False
    menetszam = 0

    bot.settings(488, 488, 488, 488)
    bot.straight(-848)
    bot.turn(-90)
    #kieg_motor_1.run_angle(777, -256, wait=False)
    #kieg_motor_2.run_angle(777, 234)
    bot.settings(101, 101, 101, 101)
    bot.straight(222)

    ''' #színszenzor használata kincshez
    while not kesz: 
        if sensor.color() == Color.WHITE or menetszam>=7:
            bot.straight(56)
            kieg_motor_2.run_angle(111, -63)
            kieg_motor_1.run_time(111, 2340)
            kesz = True
        else:
            bot.straight(23.4)
            menetszam += 1'''
    
    #kincs kiemelése
    kieg_motor_2.run_time(-67, 673)
    bot.turn(-7)

    #Junior felemelése
    kieg_motor_1.run_time(83.6, 2340)
    bot.turn(7)
    #, wait=False
    kieg_motor_1.run_time(-111, 2640)
    bot.settings(234, 234, 234, 234)

    #szobor
    bot.straight(-167)
    bot.settings(777,777,777,777)
    #kieg_motor_2.run_time(-777, 500)
    bot.turn(35)
    bot.straight(369)
    #Đbot.turn(-6.7)
    kieg_motor_1.run_time(430, 1111)
    bot.turn(-24)

    #bázisra visszatérés
    bot.straight(-333)
    bot.curve(123, 93, Stop.NONE)
    bot.straight(548)

    bot.use_gyro(False)
    
if __name__ == "__main__":
    mission1()