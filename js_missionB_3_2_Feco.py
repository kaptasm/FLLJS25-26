from js_base import bot, kieg_motor_1, kieg_motor_2

# a lelet kiemelése 
bot.straight(-430)
bot.turn(-75)
bot.turn(75)
bot.straight(50)
bot.turn(105)
bot.straight(200)
kieg_motor_2.run_angle(150, 130)
kieg_motor_2.run_angle(250,-200)
bot.straight(-50)
kieg_motor_2.run_angle(150, 150)
bot.turn(-45)
bot.straight(-800)
