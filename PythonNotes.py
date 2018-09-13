### 									PYTHON NOTES
#--------------------------------------------------------------------------------------------------
## VOWEL CHECKER
# Count the number of vowels that appear in a string, using an if statement.

x = input('Please enter a word.')

# def vowelcheck(x):
# 	count = 0
# 	if x in 'aeiou':
# 		count += 1
# 		print('There are ' + str(count) + ' vowels in this word.')
# 	else:
# 		print('There are ' + str(count) + ' vowels in this word.')

# Same problem but using a list comprehension instead.

print('There are ' + str(sum([1 for i in x if i in 'aeiou'])) + ' vowels in this word.')


