def word_count(book_text):
	count = len(book_text.split())
	return count

def char_count(book_text):
	char_dict = {}
	char_list = list(book_text)
	for char in char_list:
		char = char.lower()
		if char not in char_dict:
			char_dict[char] = 1
		else:
			char_dict[char] += 1
	return char_dict

def sort_key(items):
	return items["num"]

def sort_list(dict):
	my_list = []
	for key, value in dict.items():
		my_list.append({"char":key, "num": value})
	my_list.sort(reverse=True, key=sort_key)
	return my_list

