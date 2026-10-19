from js_alap import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission4():
    bot.use_gyro(True)
    bot.settings(777,777,777,777)
    bot.straight(-710)
    #levél vissza szállítás
    bot.settings(111,111,111,111)
    bot.turn(-20)
    bot.turn(20)
    bot.straight(110)
    bot.turn(87)
    #fára rápozícionálás
    bot.settings(777,777,777,777)
    bot.straight(-310)
    bot.settings(111,111,111,111)
    bot.turn(-87)
    #inda leemelése
    bot.straight(-110)
    kieg_motor_1.run_time(249,3000,wait=False)
    bot.straight(50)
    bot.straight(-50)
    #fa felemelése
    kieg_motor_2.run_time(999,3000)
    bot.straight(50)
    kieg_motor_2.run_time(-999,2000)
    bot.straight(-58)
    kieg_motor_2.run_time(999,2000)
    kieg_motor_2.run_time(-999,2000, wait=False)
    bot.settings(555,555,555,555)
    #mag lelökése
    bot.straight(50)
    bot.straight(-50)
    #bázisra visszatérés
    bot.straight(100)
    bot.settings(777,777,777,777)
    bot.turn(90)
    bot.straight(200)
    bot.turn(-60)
    bot.straight(600)
    bot.use_gyro(False)

if __name__ == "__main__":
    mission4()
