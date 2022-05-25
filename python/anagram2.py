# Don't forget to run the tests (and create some of your own)

def anagrams_for(word, list_of_words):
	word_chars = ''.join(sorted(word))
	match_list = []
	for i, x in enumerate(list_of_words):
		test_chars = ''.join(sorted(x))
		if(test_chars==word_chars):
			match_list.append(x)

	return match_list		
		


