def main():
    # path = input("Please enter the path to the book: ")
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    print(word_count)
    exit()

def get_text(path):
    try:
        with open(path) as f:
            return f.read()
    except:
        print("That path doesn't exist.")
        print("")
        return main()

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    text = text.lower()
    chars = {}

    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
    

main()