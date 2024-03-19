def main():
    path = input("Please enter the path to the book: ")
    # path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    dict_to_list = get_dict_to_list(char_count)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    print()
    for i in range(len(dict_to_list)):
        if dict_to_list[i]['char'].isalpha():
            print(f"The '{dict_to_list[i]['char']}' character was found {dict_to_list[i]['num']} times")
    print("--- End report ---")
    
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

def get_dict_to_list(chars):
    char_list = []

    for char,num in chars.items():
        char_list.append({'char': char, 'num': num})
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(d):
    return d["num"]

main()