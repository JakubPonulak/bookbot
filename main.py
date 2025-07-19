from stats import word_count, char_count, sort_list
import sys

if len(sys.argv) != 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
	with open(filepath) as book:
		book_contents = book.read()
		return book_contents

def main():
	count = word_count(get_book_text(filepath))
	char_dict = char_count(get_book_text(filepath))
	sorted_list = list(filter(lambda x: x["char"].isalpha() == True, sort_list(char_dict)))
	print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\nFound {count} total words\n--------- Character Count -------")
	for item in sorted_list:
		print(f"{item["char"]}: {item["num"]}")

main()
