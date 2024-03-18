def main():
    # path = input("Please enter the path to the book: ")
    path = "books/frankenstein.txt"
    text = get_text(path)
    wc = get_word_count(text)
    print(wc)
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
    return (len(text.split()))

main()