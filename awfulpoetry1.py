import random

articles = ['the', 'a', 'another']
objects = ['cat', 'dog', 'horse', 'man', 'woman', 'boy', 'girl']
verbs = ['sang', 'ran', 'jumped', 'laughed', 'hoped']
adverbials = ['loudly', 'quietly', 'well', 'badly', 'rudely']

i = 0
while i < 5:
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