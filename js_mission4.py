from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission4():
    bot.use_gyro(True)
    bot.settings(355,355,355,355)
    #Kovácsműhely(06),Bázisról elindulás
    kieg_motor_2.run_angle(100,-90,wait=False)
    bot.straight(743)
    bot.settings(150, 150, 150, 150)
    bot.turn(-62)
    #Ki lakott itt(05)
    bot.settings(565,565,565,565)
    bot.straight(55)
    bot.turn(-13)
    bot.turn(23)
    #Nehézemelés(07), kavicsok kitolása
    bot.straight(-135)
    bot.turn(-42)
    bot.straight(-120)
    #Nehéz emelés(07)
    kieg_motor_2.run_angle(120, 90)
    bot.straight(-190)
    bot.settings(777,777,777,777)
    bot.turn(-3.6)
    bot.straight(100, Stop.NONE)
    kieg_motor_2.run_angle(777, -90, wait=False)
    #bot.turn(-10)
    bot.straight(390)
    #Bázisra visszatérés
    bot.turn(-120)
    bot.straight(700)
    bot.use_gyro(False)

if __name__ == "__main__":
    mission4()