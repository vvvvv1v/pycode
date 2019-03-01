import random

articles = ['the', 'a', 'another']
objects = ['cat', 'dog', 'horse', 'man', 'woman', 'boy', 'girl']
verbs = ['sang', 'ran', 'jumped', 'laughed', 'hoped']
adverbials = ['loudly', 'quietly', 'well', 'badly', 'rudely']

number = 0
while True:
	try:
		string = input('enter a number or Enter for 5: ')
		if not string:
			number = 5
			break
		number = int(string)
		if 1 <= number <= 10:
			break
		else:
			print('number must between 1 and 10')
	except ValueError as err:
		print(err)

i = 0
while i < number:
	article = random.choice(articles)
	object = random.choice(objects)
	verb = random.choice(verbs)
	adverbial = random.choice(adverbials)
	choice = random.randint(1, 2)
	line = article + ' ' + object + ' ' + verb + ' '
	if choice == 1:
		line += adverbial
	else:
		pass
	print(line)
	i += 1