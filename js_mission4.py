from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission4():
    #Kovácsműhely(06),Bázisról elindulás
    kieg_motor_2.run_angle(100,-90)
    bot.straight(736)
    bot.turn(-62)
    #Ki lakott itt(05)
    bot.straight(67)
    bot.turn(-10)
    bot.turn(20)
    #Nehézemelés(07), kavicsok kitolása
    bot.straight(-150)
    bot.turn(-42)
    bot.straight(-120)
    #Nehéz emelés(07)
    kieg_motor_2.run_angle(120, 90)
    bot.straight(-190)
    bot.straight(60)
    kieg_motor_2.run_angle(130, -90)
    bot.turn(-10)
    bot.straight(414)
    #Siló(08)
    bot.turn(-175)
    bot.straight(42.2)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    kieg_motor_1.run_time(777,800)
    kieg_motor_1.run_time(-777,800)
    bot.settings(777,777,777,777)
    #Bázisra visszatérés
    bot.turn(55)
    bot.straight(700)

if __name__ == "__main__":
    mission4()