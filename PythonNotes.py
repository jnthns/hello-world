# def vwl(s):
# 	count = 0
# 	if s == '':
# 		print('Re-enter word.')
# 	elif s in 'aeiou':
# 		count += 1
# 		print('There are ' + str(count) + ' vowels in this word.')
# 	else:
# 		print("There are " + str(count) + " vowels in this word.")


# def vowel(x):
# 	count = 0
# 	for letter in x:
# 		if letter in 'aeiou':
# 			count += 1
# 			print('There are ' + str(count) + ' vowels in this word.')
# 		else:
# 			print('There are ' + str(count) + ' vowels in this word.')
# 			break


x = 'jon'
print('There are ' + str(sum([1 for i in x if i in 'aeiou'])) + ' vowels in this word.')


sum([1 for i in x if i in 'aeiou'])
