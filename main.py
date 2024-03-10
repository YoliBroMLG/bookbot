def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = calc_word_count(text)
    character_count = calc_character_count(text)
    print(word_count) 
    print(character_count)

def calc_word_count(text):
    words = text.split()
    return len(words)

def calc_character_count(text):
    characters = {}
    for character in text:
        lowered_character = character.lower()
        if lowered_character in characters:
            characters[lowered_character] += 1 
        else:
            characters[lowered_character] = 0
    return characters 

    return lowered_text

def get_book_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

main()