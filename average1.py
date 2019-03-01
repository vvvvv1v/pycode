numbers = []
count = 0
sum = 0
lowest = 0
highest = 0
mean = 0

while True:
	try:
		string = input('enter a number or Enter to finish: ')
		if not string:
			break
		number = int(string)
		if count == 0:
			lowest = number
			highest = number
		else:
			if number < lowest:
				lowest = number
			if number > highest:
				highest = number
		numbers.append(number)
		count += 1
		sum += number
	except ValueError as err:
		print(err)
if count == 0:
	print('no input.')
else:
	print('numbers:', numbers)
	print('count =', count, 'sum =', sum, 'lowest =', lowest, 'highest =', highest, 'mean =', sum / count)