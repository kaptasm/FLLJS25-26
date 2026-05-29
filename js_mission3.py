from js_base import bot, kieg_motor_1, wait

def mission3():
    bot.use_gyro(True)
    '''bot.use_gyro(True)
    ismetles = 0'''
    bot.settings(546, 546, 546, 546)
    #tololap betolasa
    bot.straight(475)
    #zászló kiszállítás
    kieg_motor_1.run_angle(777, 110)
    #homok lehúzása
    bot.turn(11.11)
    bot.straight(-111)
    #Kék bázisra átjutás
    bot.settings(777, 777, 777, 777)
    bot.turn(-46)
    bot.straight(363)
    bot.turn(44)
    bot.straight(999)
    '''bot.turn(76)
    bot.straight(52)
    bot.turn(-3)
    bot.use_gyro(False)
    while ismetles!=10:
        bot.turn(-28)
        bot.turn(27)
        ismetles+=1
    bot.use_gyro(True)
    bot.turn(-7)
    bot.straight(-69)
    bot.turn(-69)
    bot.straight(730)'''
    bot.use_gyro(False)

if __name__ == "__main__":
    mission3()