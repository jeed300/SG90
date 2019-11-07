import pigpio
import time

pi = pigpio.pi()


def setup():
	pi.set_servo_pulsewidth(4, 1300) #armall center1300
	time.sleep(3)
	pi.set_servo_pulsewidth(13, 2000) #armhight 1500
	time.sleep(3)
	pi.set_servo_pulsewidth(5, 1500) #arm position
	time.sleep(3)
	pi.set_servo_pulsewidth(6,1500) #arm grab
	time.sleep(3)
	
def main():
	print("setup start...")
	setup()
	print("setup end...")
	
	print("A start!")

	print("arm get start...")

	pi.set_servo_pulsewidth(4,1300)
	time.sleep(3)	
	pi.set_servo_pulsewidth(13, 1500)
	time.sleep(3)
	pi.set_servo_pulsewidth(5, 1000)
	time.sleep(3)
	pi.set_servo_pulsewidth(6,800)
	time.sleep(3)
	
	print("A arm get end...")