import random
print('Вас приветсвует казино 3 топора...')
number_random = random.randint(1, 5)
number_player = input('Введите число: ')

if number_random == int(number_player):
	print(' $$$ ')
else:
	print('  GAME OVER ')
	print(' - 100 $ ')
