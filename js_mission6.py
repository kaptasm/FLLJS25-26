from js_alap import nav_motor_1,nav_motor_2, kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission6(): 
    bot.use_gyro(True)

    bot.settings(777,777,777,777)
    bot.turn(-35)
    # ráfordulás a háloba
    bot.straight(-205)
    bot.turn(35)
    bot.straight(-615)
        # hátra,jövetel
    bot.straight(130)
    # ráfordulás a kiöntésre
    bot.turn(50)
    bot.straight(-236.7)
    # kiöntés
    kieg_motor_2.run_angle(600,100)
    bot.turn(20)
    # fa emelése
    kieg_motor_1.run_angle(600,180)
    bot.straight(150)
    # vissza navigálás a bázisra
    bot.turn(-71)
    bot.straight(700)

    bot.use_gyro(False)


if __name__ == "__main__":
    mission6()
