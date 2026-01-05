from js_base import kieg_motor_1, kieg_motor_2, bot, wait, Stop

def mission1():
    '''bot.settings(333, 333, 333, 333)
    bot.straight(756)
    bot.turn(-39)
    kieg_motor_1.run_angle(248, -248)
    bot.straight(55)
    bot.straight(-22)
    kieg_motor_1.run_angle(135, 135)
    bot.straight(22)
    bot.straight(-11)
    bot.straight(33)
    kieg_motor_1.run_angle(155, -55)
    kieg_motor_1.run_angle(169, 169)
    kieg_motor_1.run_angle(269, 269)
    bot.straight(-69)
    bot.turn(22)
    bot.straight(48)
    bot.turn(111)
    bot.turn(-111)
    #bot.straight(-76)
    bot.turn(111)
    bot.straight(11)
    bot.turn(-28)
    bot.straight(250)
    bot.turn(28)
    bot.straight(23)
    #bot.turn(-90)
    #bot.straight(-90)
    kieg_motor_2.run_time(248, 1000)
    kieg_motor_2.run_time(-101, 2888)
    #bot.straight(11)
    kieg_motor_2.run_time(-101, 2222)
    bot.straight(-33)
    kieg_motor_2.run_time(260, 1000)
    bot.straight(59)
    bot.turn(-111)
    bot.straight(-44)
    bot.turn(-48)
    bot.straight(16)
    bot.turn(-44)
    kieg_motor_2.run_angle(111, -111)
    bot.turn(-16)
    bot.turn(22)
    kieg_motor_2.run_angle(111, -111)
    bot.turn(-82)
    bot.straight(-505)
    bot.settings(99, 99, 99, 99)
    bot.turn(-85)
    bot.straight(-666)'''

    
    bot.settings(222, 222, 222, 222)
    bot.straight(-69)
    bot.turn(44)
    bot.straight(-139)
    bot.turn(-44)
    bot.straight(-595)
    bot.turn(-91)

    bot.settings(111, 111, 111, 111)
    bot.straight(199)
    kieg_motor_1.run_angle(111, 302.4)
    kieg_motor_2.run_angle(111, -52)
    bot.turn(-3.9)
    bot.straight(-108)
    bot.turn(97)
    kieg_motor_2.run_angle(111, -55)
    
    bot.settings(777, 777, 777, 777)
    bot.straight(155)
    bot.turn(20)
    bot.settings(370,370,370,370)
    bot.straight(400)
    bot.settings(777, 777, 777, 777)
    bot.straight(-300)
    bot.turn(-76)
    bot.straight(-100)
    bot.turn(15)
    bot.straight(-90)
    bot.turn(-16)
    bot.straight(170)
    bot.turn(-40)
    bot.straight(120)
    bot.turn(127)
    bot.straight(700)
    

    '''bot.settings(777,777,777,777)
    bot.turn(58)
    bot.straight(250)
    bot.turn(75)
    bot.straight(250)
    bot.straight(-100)
    bot.turn(-90)
    bot.straight(1000)'''
    #bot.settings(355, 355, 355, 355)
    #bot.settings(555,555,555,555)
    #bot.straight(-230)
    #bot.turn(-12)
    #bot.settings(777,777,777,777)
    #bot.straight(300)
    #bot.turn(67)
    #bot.straight(555)
    #bot.straight(120)
    #bot.turn(-50)

    #kieg_motor_1.run_time(500, 100000)
    
if __name__ == "__main__":
    mission1()

'''
import pygame
import time
import board
from adafruit_ads1x15 import ADS1015, AnalogIn, ads1x15

pygame.init()
pygame.mixer.init()

i2c = board.I2C()
ads = ADS1015(i2c)
chan = AnalogIn(ads, ads1x15.Pin.A0)
pygame.mixer.music.load('/home/raspberrypi/Music/lkh.mp3')
vol = 0.0
pygame.mixer.music.set_volume(vol)
pygame.mixer.music.play(-1)

try:
   
#try:  
    while True:
        
       vol = chan.voltage
       if vol >= 0.1 :
           vol = vol/2
           pygame.mixer.music.set_volume(vol)
           print(f"{chan.value:>5}\t{chan.voltage:>5.3f}\t{vol}")
           time.sleep(0.5)
           pygame.mixer.music.set_volume(0)
       else:
           pygame.mixer.music.set_volume(0) 
except pygame.error as e:
    print(f"Hiba lajatszaskor: {e}")

finally:
    pygame.mixer.quit()
    pygame.quit()'''


