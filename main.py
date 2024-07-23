def main():
    book_path = 'books/frankenstein.txt'
    book = get_book_text(book_path).lower()
    word_count = count_words(book)
    words = text_words(book)

    char_map = {}
    for word in words:
        insert_char_count_into_map(char_map, word)

    print(f'The book has {word_count} words')
    print(char_map)


def get_book_text(path):
    with open(path) as file:
        return file.read()


def count_words(text):
    return len(text.split())


def text_words(text):
    return text.split()


def insert_char_count_into_map(char_map: dict, word: str):
    for char in word:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1


main()
