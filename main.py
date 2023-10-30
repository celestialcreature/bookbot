def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = get_book_wordcount(text)
    print(f"there are {wordcount} words in this book")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_book_wordcount(text):
    words = text.split()
    wordcount = len(words)
    return wordcount


main()