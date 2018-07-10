import os
import time
def s1():
	os.system('cls')
	print('You are going to college. \nHow do you reach station?\n\n')
	print('1. Take the cycle')
	print('2. Take the bus')
	print('3. Take the train')
	print('\n>>>',end='')
	i=int(input())
	if i== 1:
		os.system('cls')
		print('You cant take the cycle. It is broken')
		time.sleep(3)
		s1()
	elif i == 2:
		os.system('cls')
		print('You cant take the bus. It takes 3 hrs')
		time.sleep(3)
		s1()
	elif i == 4:
		exit()
	else:
		s2()
def s2():
	os.system('cls')
	print('Now you have reached the station. You need to go to Chuchura')
	print('Which platform do you need to go? (1/2/3/4)')
	print('\n>>>',end='')
	i=int(input())
	if i == 1:
		os.system('cls')
		print('No You idiot.Its the wrong direction')
		time.sleep(3)
		s2()
	elif i == 2:
		os.system('cls')
		print('WROOOONG DIRECTION....!!!!')
		time.sleep(3)
		s2()
	elif i == 3:
		os.system('cls')
		print('Great . Now you have reached Chuchura')
		time.sleep(3)
		os.system('cls')
		print('Thanks for playing the demo.\n And my name is NOT Alaphan')
		time.sleep(5)

	else:
		os.system('cls')
		print('Right Direction, Wrong Line')
		time.sleep(3)
		s2()
		


s1()