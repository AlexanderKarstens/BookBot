"""
Book reader
"""
import os

#This variable give the PATH to the functions where all the book will be stored
BASE_DIR = "./books"

def main():
    """
    Main function

    Uses alot of print to make the options in the console
    It's also using a try statement to make sure the user is picking a valid options to pick from 
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
            #All the prints are making the options to chose from in the console 
            print("Options:")
            print(f"a read book")
            print(f"b count words")
            print(f"c count letters")
            opt = input("Select option: ")
            book = books[int(idx)]
            contents = readfile(book)
            #Reads and print out the chosen book
            if opt == "a": 
                clear_screen()
                print(f"Reading {book}:")
                print(contents)
            #Counts the number of words in the chosen book
            elif opt == "b": 
                clear_screen()
                words = contents.split()
                print(f"counting word: {len(words)}")
            #Count how many if each letter that are in the chosen book
            elif opt == "c":  
                clear_screen()
                words = contents.split()
                generate_report(book, words)            
    except Exception as e:
         main()

def sort(letter_counts):
    """
    Sorts the letters

    Args: 
    * letter_count (String): A string of all the letters in the book

    Return:
    * Return a list with the letter_counts count in a string to use in a dict
    """
    return letter_counts["count"]


def count_letters(letter, words):
    """
    Gets the number of occurrences of a specific letter in a list of words.

    Args:
    * letter (char): Letter to count
    * words (List[str]): A list of strings to count occurences of letter

    Return:
    * Returns a dict that contains a letter and the number of that letter
    """
    count = 0
    for word in words:
        for w in word:
            if w.lower() == letter:
                count += 1
    return {"letter": letter, "count": count}


def generate_report(book, words):
    """
    Generates the final report of how many of each letters there are in use

    Args:
    * book (List[str]): A list of string from the file 
    * words (List[str]): A list of strings to count occurences of letter

    Return:
    * prints out the end result of the report and make it look nice and clean
    """
    letter_counts = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in alphabet:
        letter_dict = count_letters(letter, words)  
        letter_counts.append(letter_dict)    
    #This is sorting the list of letters in order of what have the highest count    
    letter_counts.sort(reverse=True, key=sort)
    #Print statements to make the final report
    print(f"--- Begin report of {book.replace('.txt', '').capitalize()} ---")
    print(f"{len(words)} words found in the document")
    print("")
    for letter_dict in letter_counts:
        print(f"The '{letter_dict['letter']}' character was found {letter_dict['count']} times")
    print("--- End report ---")

def clear_screen():
    """
    Clear the screen

    This function clears the consol, and it does it between every step
    """
    os.system("cls" if os.name == "nt" else "clear")

def is_valid_index(idx, length):
    """
    Check if the index is valid

    This function checks if the input is a number and if its higher then zero and lower then length of the list
    """
    return idx in "0123456789" and int(idx) >= 0 and int(idx) < length

def readfile(file_path):
    """
    Reads the contents of a file

    Args:
    * file_path (string): The path to the file 
    Returns:
    * contents: return one big string out for the program to read it
    """
    with open(os.path.join(BASE_DIR, file_path)) as file:
        contents = file.read()
        return contents

if __name__ == "__main__":
    main()