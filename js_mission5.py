from js_alap import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission5(): 
    bot.use_gyro(True)

    
    #drón felemelés, betolás
    bot.settings(321,321,321,321)
    bot.straight(-665)
    bot.settings(111, 111, 111, 111)
    bot.turn(-20)
    bot.straight(-10)
    bot.turn(10)
    bot.settings(777,777,777,777)
    #bot.straight(20)
    bot.turn(-40)
    #daisy kiszállítása
    #bot.turn(35)
    bot.turn(25)
    bot.straight(40)
    bot.turn(25)
    bot.straight(40)
    #bot.straight(120)
    bot.straight(160)
    bot.settings(111, 111, 111, 111)
    bot.turn(-50)
    bot.settings(777,777,777,777)
    #kieg_motor_1.run_time(-777,700)
    bot.straight(-390)
    kieg_motor_2.run_time(777,2000)
    bot.straight(110)
    bot.turn(26)
    #gyökér mag leszedés
    bot.straight(-370)
    kieg_motor_1.run_time(144,1100)
    bot.straight(90)
    bot.turn(-27)
    bot.settings(777,777,777,777)
    
    bot.straight(-230)
    bot.turn(-10)
    bot.straight(-170)

    #levelekre fordulás:
    bot.settings(111,111,111,111)
    bot.straight(-210)
    bot.settings(567,567,567,567)

    bot.straight(85)
    bot.turn(100)
    kieg_motor_1.run_time(-111,2500,wait=False)
    
    bot.straight(-200)
    bot.straight(200)
    
    bot.turn(-15)
    kieg_motor_2.run_time(-777,2000,wait=False)
    #kieg_motor_1.run_time(-777,450)

    bot.straight(-240)
    bot.turn(-35)
    bot.settings(111,111,111,111)
    bot.straight(-178)
    bot.settings(777,777,777,777)
    kieg_motor_1.run_time(700,600,wait=False)
    bot.straight(40)
    bot.turn(80)
    bot.straight(-550)

    ''' 
    bot.turn(90)
    bot.straight(-80)
    bot.turn(19)
    bot.settings(567,567,567,567)
    bot.straight(-130)
    bot.turn(-50, wait=False)
    kieg_motor_2.run_time(-777,2000,wait=False)
    kieg_motor_1.run_time(-777,450)
    bot.straight(-80)
    bot.turn(-18)
    bot.straight(-100)
    kieg_motor_1.run_time(700,600,wait=False)
    bot.straight(30)
    bot.turn(90)
    bot.straight(-550)'''
    
    bot.use_gyro(False)

if __name__ == "__main__":
    mission5()
