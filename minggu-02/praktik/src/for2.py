words = ['cat', 'window', 'defenestrate']
for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)
words