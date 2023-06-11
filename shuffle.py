import random, sys
'''
Shuffles words to be learned, kinda like flash cards.
Current implementation is you pass a file as an argument with a list of words.
These words will be output in random order where each word is separated by a
new line.

Usage: python3 shuffle.py word_file
'''

def shuffle_from_args(args):
	'''
	args are the words to be shuffled. Returns a string with each word
	separated by a newline and in random order (i.e. a different order
	than the sequence in args).
	'''
	word_list = [args[i] for i in range(1, len(args))]
	random.shuffle(word_list)

	## return a string where each word is separated by a newline
	return "\n".join(word_list)

def shuffle_from_word_file(file):
	'''
	Returns a list of words from the file in random order. Words in a file are
	separated by new lines
	'''
	word_list = open(word_file).read().splitlines()
	random.shuffle(word_list)

	## return a string where each word is separated by a newline
	return "\n".join(word_list)

def shuffle_from_word_list(word_list):
	'''
	Returns a list of the words in word_list in randomized order
	'''
	word_list_copy = [word for word in word_list]
	random.shuffle(word_list_copy)

	## return a string where each word is separated by a newline
	return "\n".join(word_list)

if __name__ == '__main__':
	# Usage: python3 shuffle.py word_file
	word_file = sys.argv[1]
	print(shuffle_from_word_file(word_file))
