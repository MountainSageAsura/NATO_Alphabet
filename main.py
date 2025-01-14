import pandas

data_file = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# e.g. {"A": "Alfa", "B":"Bravo"}
# for (index, row) in data_file.iterrows():
#     print(row.letter)
#     print(row.code)

# use dictionary comprehension to create new dictionary with the letter as key and word as value
# letter column is named letter
# word column is named code
# .iterrows() is used to iterate through each row
nato_dict = {row.letter:row.code for (index, row) in data_file.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_list():
    """This function asks user for input and handles errors.
    If the user input is valid it prints the phonetic list"""
    user_input = input("Enter a word: ").upper()
    try:
        if len(user_input) == 0:
            raise KeyError
        phonetic_list = [nato_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_list()
    else:
        print(phonetic_list)

generate_list()