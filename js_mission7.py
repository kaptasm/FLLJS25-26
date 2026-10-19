from js_alap import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

"""bot.settings(777,777,777,777)
bot.straight(-110)
bot.turn(-66.5)
bot.straight(-361)
kieg_motor_1.run_angle(180,134)
bot.turn(-11)
bot.straight(-175)
kieg_motor_1.run_angle(50,85)
kieg_motor_1.run_angle(50,-90)
bot.straight(8)
bot.turn(7.5)
bot.straight(-55)
kieg_motor_1.run_angle(100,-150)"""
'''

    bot.settings(555,555,555,555)
    kieg_motor_2.run_angle(300,-65)
    kieg_motor_1.run_angle(300,-200,wait=False)
    #navigálás A feladathoz 
    bot.straight(-325)
    #csapóajtó lecsapás
    #bal kar felemel
    kieg_motor_2.run_time(200,555)
    wait(500)
    bot.straight(20)
    kieg_motor_2.run_angle(200,-150)
    kieg_motor_1.run_angle(200,180)
    bot.straight(-30)
    # #bal kar le
    # kieg_motor_2.run_time(-155,700)
    # wait(500)
    # #jobb kar fel
    # kieg_motor_1.run_time(360,770)
    # bot.straight(110)
    # #behuzni az ablakos cuccot
    # kieg_motor_1.run_time(-400,625)
    # bot.straight(330)
    # #vissza a bazisra'''


def mission7():


    bot.settings(777,777,777,777)
    kieg_motor_2.run_angle(300,-65)
    kieg_motor_1.run_angle(300,-300,wait=False)
    #navigálás A feladathoz 
    bot.straight(-400)
    kieg_motor_2.run_angle(777,200,wait=False)
    kieg_motor_1.run_angle(300,200)
    bot.turn(-3)
    bot.straight(40)
    kieg_motor_2.run_angle(777,-200)
    kieg_motor_2.run_angle(120,200)

    bot.straight(250)

'''bot.settings(777,777,777,777)
kieg_motor_2.run_angle(300,-65)
kieg_motor_1.run_angle(300,-300)
'''

if __name__ == "__main__":
    mission7()
