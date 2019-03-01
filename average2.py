numbers = []
count = total = lowest = highest = mean = median = 0
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
		total += number
	except ValueError as err:
		print(err)

if count == 0:
	print('no input.')
else:
	print('numbers:', numbers)
	flag = True
	i = 0
	while i < len(numbers) - 1 and flag:
		j = 0
		flag = False
		while j < len(numbers) - 1 - i:
			if int(numbers[j]) > int(numbers[j + 1]):
				temp = numbers[j]
				numbers[j] = numbers[j + 1]
				numbers[j + 1] = temp
				flag = True
			j += 1
		i += 1
	if len(numbers) % 2 == 0:
		median = (int(numbers[int(len(numbers) / 2 - 1)]) + int(numbers[int(len(numbers) / 2)])) / 2
	else:
		median = int(numbers[int(len(numbers) / 2 - 0.5)])
	print('count =', count, 'sum =', total, 'lowest =', lowest, 'highest =', highest, 'mean =', total / count, 'median =', median)