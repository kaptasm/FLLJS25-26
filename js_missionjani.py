from js_base import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

#navigálás az ecsethez
kieg_motor_2.run_angle(200, -136)
bot.straight(310)

#ecset megcsinálás
kieg_motor_2.run_angle(200, 50)
bot.straight(100)
bot.straight(-150)
bot.straight(100)
bot.turn(-45)

#navigálás a bánya kocsihoz
bot.turn(93)
bot.straight(500)

#bánya kocsi emelés
kieg_motor_2.run_angle(200, 45)
bot.straight(-300)
bot.turn(-40)
bot.straight(450)











'''kieg_motor_2.run_angle(400,-280)
bot.straight(720)
bot.turn(-41)
bot.straight(270)
kieg_motor_2.run_angle(200,250)
kieg_motor_2.run_angle(200,-200)
bot.turn(42)
kieg_motor_2.run_angle(100,250)
nav_motor_2.run_angle(200,350)
bot.straight(-130)
nav_motor_1.run_angle(200,-240)

kieg_motor_2.run_angle(200,-200)
bot.turn(-60)
bot.straight(250)
bot.turn(-90)
bot.straight(750)
bot.turn(45)
bot.straight(100)'''