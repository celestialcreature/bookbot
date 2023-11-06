def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_book_wordcount(text)
    character_dict = get_character_count(text)
    sorted_characters = sort_character_count(character_dict)
    
    print(f"--- Begin report of {book_path} ---\nthere are {wordcount} words in this book\n")
    for item in sorted_characters:
        print(f"The '{item['character']}' character was found {item['num']} times")
    print("\n--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_wordcount(text):
    words = text.split()
    wordcount = len(words)
    return wordcount


def sort_on(d):
    return d["num"]

def sort_character_count(character_count_dict):
    sorted_list = []
    for char in character_count_dict:
        sorted_list.append({"character": char, "num": character_count_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    
def get_character_count(text):
    characters = {}
    for letter in text.lower():
        if letter.isalpha() == True:
            if letter in characters:
                characters[letter] += 1
            else:
                characters[letter] = 1
    return characters



main()