from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission4():
    #Kovácsműhely(06),Bázisról elindulás
    kieg_motor_2.run_angle(100,-90,wait=False)
    bot.straight(743)
    bot.turn(-62)
    wait(500)
    #Ki lakott itt(05)
    bot.settings(565,565,565,565)
    bot.straight(66)
    bot.turn(-13)
    bot.turn(23)
    #Nehézemelés(07), kavicsok kitolása
    bot.straight(-162)
    bot.turn(-42)
    bot.straight(-120)
    #Nehéz emelés(07)
    kieg_motor_2.run_angle(120, 90)
    bot.straight(-190)
    bot.settings(777,777,777,777)
    bot.straight(100)
    kieg_motor_2.run_angle(130, -90)
    #bot.turn(-10)
    bot.straight(390)
    #Bázisra visszatérés
    bot.turn(-120)
    bot.straight(700)

if __name__ == "__main__":
    mission4()