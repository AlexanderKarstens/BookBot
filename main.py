"""
Book reader
"""
import os

#This variable give the PATH to the functions where all the book will be stored
BASE_DIR = "./books"

def main():
    """
    Main function
    """
    clear_screen()
    print("Book reader")
    books = os.listdir(BASE_DIR)
    for i, book in enumerate(books):
        print(f"{i} {book}")

    idx = input("Select a book: ")

#This exception uses the checks to se if it a correct input
#and give option to pick what to do with the chosen book 
    try: 
        if is_valid_index(idx, len(books)):
            clear_screen()
            print("Options:")
            print(f"a read book")
            print(f"b count words")
            print(f"c count letters")
            opt = input("Select option: ")
            book = books[int(idx)]
            contents = readfile(book)
            if opt == "a": #Reads and print out the chosen book
                clear_screen()
                print(f"Reading {book}:")
                print(contents)
            elif opt == "b": #Counts the number of words in the chosen book
                clear_screen()
                words = contents.split()
                print(f"counting word: {len(words)}")
            elif opt == "c": #Count how many if each letter that are in the chosen book 
                clear_screen()
                words = contents.split()
                generate_report(book, words)            
    except Exception as e:
         main()

#
def sort(letter_counts):
    return letter_counts["count"]

#
def count_letters(letter, words):
    count = 0
    for word in words:
        for w in word:
            if w.lower() == letter:
                count += 1
    return {"letter": letter, "count": count}

#
def generate_report(book, words):
    letter_counts = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        letter_dict = count_letters(letter, words)  
        letter_counts.append(letter_dict)        
    letter_counts.sort(reverse=True, key=sort)
    print(f"--- Begin report of {book.replace('.txt', '').capitalize()} ---")
    print(f"{len(words)} words found in the document")
    print("")
    for letter_dict in letter_counts:
        print(f"The '{letter_dict['letter']}' character was found {letter_dict['count']} times")
    print("--- End report ---")


#This function clears the consol, and it does it between every step
def clear_screen():
    """
    Clear the screen
    """
    os.system("cls" if os.name == "nt" else "clear")

#This function checks if the input is a number and if its higher then zero and lower then length of the list
def is_valid_index(idx, length):
    """
    Check if the index is valid
    """
    return idx in "0123456789" and int(idx) >= 0 and int(idx) < length

#This function reads the file from the given PATH and then returns the content out of the file 
def readfile(file_path):
    """
    Read the contents of a file
    """
    with open(os.path.join(BASE_DIR, file_path), encoding="utf-8") as file:
        contents = file.read()
        return contents

if __name__ == "__main__":
    main()