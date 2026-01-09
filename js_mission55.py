from js_base import bot, kieg_motor_1, kieg_motor_2

def mission5():
  
    bot.settings(600, 600, 600, 600)
    kieg_motor_2.run_angle(100,60)
    bot.straight(185) #bot.straight(195)
    bot.turn(-47)
    bot.straight(194)
    bot.turn(-33)#bot.turn(-40)
    kieg_motor_1.run_angle(150, -150)
    bot.turn(29)
    bot.straight(230)#bot.straight(190)
    kieg_motor_2.run_angle(150,-70)
    kieg_motor_2.run_angle(150,100,wait=False)
    kieg_motor_1.run_angle(240, 200)
    bot.turn(-10)
    bot.straight(-166)#bot.straight(-176)
    #bot.straight(20)
    #bot.straight(33)
    kieg_motor_1.run_angle(300,-220)
    bot.straight(-15)
    bot.turn(-28.5)
    bot.straight(170)
    bot.settings(600, 600, 600, 600)
    kieg_motor_1.run_angle(200, 180)
    #kieg_motor_1.run_angle(777,155)
    #a vödör kihúzás
    bot.settings(650, 650, 650, 650)
    bot.turn(-50)
    #vissza navigálás
    bot.settings(888, 888, 888, 888)
    bot.turn(-90)
    bot.straight(380)
    
if __name__ == "__main__":
    mission5()