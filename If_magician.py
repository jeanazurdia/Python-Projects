#learning if statements w/elif, else

is_magician = False
is_expert = True

if is_magician and is_expert:
	print('you are a master magician')

elif is_magician > is_expert:     #elif is_magician and not is_expert
	print("at least you're getting there")
else:     #elif not is_magician
  print('You need magic powers')
