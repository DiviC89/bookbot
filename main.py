import re

def main():
    path = "./books/frankenstein.txt"
    content = read_file(path)
    word_count = count_words(content)
    char_dict = get_char_dict(content)

    print("--- Report of books/frankenstein ---")
    print(f"{word_count} words were found in the document.")
    print("")
    print("Most common letters (asc order):")
    for letter in char_dict:
        print(f"The letter '{letter}' was found {char_dict[letter]} throughout this book")
    print("--- End Report ---")


def read_file(path):
    with open(path) as f:
        content = f.read()
        f.close()
        return content

def count_words(text):
    return len(text.split())

def get_char_dict(text):
    occurence_dict = {}
    pattern = re.compile("[a-z]+")
    for c in text:
        lowered = c.lower()
        if not bool(pattern.fullmatch(lowered)):
            pass
        elif lowered in occurence_dict:
            occurence_dict[lowered] += 1
        else:
            occurence_dict[lowered] = 1
    return dict(reversed(sorted(occurence_dict.items(), key=lambda item: item[1])))


main()
