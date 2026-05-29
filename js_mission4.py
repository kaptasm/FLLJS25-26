from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission4():
    bot.use_gyro(True)
    bot.settings(555,555,555,555)
    #Kovácsműhely(06),Bázisról elindulás
    kieg_motor_2.run_angle(100,-90,wait=False)
    bot.straight(748)
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
    #bot.turn(-120)
    bot.turn(-169)
    bot.straight(57.6)
    #Siló lecsapás
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(888,800)
    #Kék bázisra visszatérés
    bot.turn(60)
    bot.straight(700)
    bot.use_gyro(False)

    
if __name__ == "__main__":
    mission4()

'''from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission4():
    bot.settings(555,555,555,555)
    bot.turn(-25)
    bot.straight(563)
    bot.settings(222,222,222,222)
    bot.turn(77)
    bot.straight(170)
    bot.settings(567,567,567,567)
    bot.turn(-33)
    bot.settings(222,222,222,222)
    kieg_motor_2.run_angle(300,-190)
    bot.turn(17.3)
    bot.straight(67)
    kieg_motor_2.run_angle(200,190)
    bot.settings(565,565,565,565)
    bot.straight(-180)
    bot.turn(-42)
    bot.straight(68)
    bot.turn(-90)
    bot.turn(42)
    bot.straight(-200)
    bot.turn(50)
    bot.straight(60)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(888,800)
    bot.turn(80)
    bot.straight(500)

if __name__ == "__main__":
    mission4()'''