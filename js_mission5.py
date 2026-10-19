from js_alap import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission5(): 
    bot.use_gyro(True)



#fokot megcsinálni a mag begyűjtéshez + egy két cente előre menet a lassú betolásnál

#drón
kieg_motor_1.run_angle(800,300)
bot.turn(10.3)
bot.settings(550,550,550,550)
bot.straight(-650)
bot.turn(-72)
bot.settings(40, 40, 40, 40)
bot.turn(59)
bot.settings(400, 400, 400, 400)
#navigálás a daisy ledobáshoz
bot.straight(280)
bot.turn(-42)
bot.straight(-480)
#daisy ledobása
kieg_motor_2.run_angle(400,120)
bot.turn(44)
kieg_motor_1.run_time(-670, 670)
#az 1. mag begyujtese
bot.straight(-135)
bot.turn(-52.5)
bot.straight(20)
bot.settings(90,90,90,90)
kieg_motor_1.run_time(150, 700)
bot.straight(20)
bot.turn(-8.5)
bot.settings(777, 777, 777, 777)
bot.straight(-450)
bot.settings(90, 90, 90, 90)
bot.straight(-50)
bot.straight(50)
bot.turn(10)
bot.straight(-250)
kieg_motor_1.run_time(300, 250, wait=False)
bot.settings(90, 90, 90, 90)
#hangya betolás
bot.settings(500,500,500,500)
bot.straight(100)
bot.turn(88)
bot.straight(-125)
bot.turn(-56)
kieg_motor_1.run_angle(450,-250)
bot.straight(-160)
kieg_motor_1.run_angle(450,250)
bot.turn(90)
bot.settings(500,500,500,500)
bot.straight(-600)

bot.use_gyro(False)

if __name__ == "__main__":
    mission5()























#SIKSZ SZEVÖN!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
