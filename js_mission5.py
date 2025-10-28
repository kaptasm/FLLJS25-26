from js_base import kieg_motor_1, kieg_motor_2, bot, Stop

#homok kihúzás
kieg_motor_2.run_angle(200,-200)
bot.straight(410)
kieg_motor_2.run_angle(200,200)
bot.straight(-70)
kieg_motor_2.run_angle(200,-200)
bot.straight(320)
bot.straight(-500)


