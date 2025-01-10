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
user_input = input("Enter a word: ").upper()
phonetic_list = [nato_dict[letter] for letter in user_input]
print(phonetic_list)