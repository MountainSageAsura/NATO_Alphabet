# NATO Phonetic Alphabet Converter

This project converts a user-inputted word into its corresponding NATO phonetic alphabet representation using a CSV file that contains the phonetic codes for each letter.

## Description

The program performs the following tasks:
1. Loads a CSV file containing the NATO phonetic alphabet into a Pandas DataFrame.
2. Constructs a dictionary where the keys are letters of the alphabet, and the values are their corresponding phonetic code words.
3. Prompts the user to input a word and converts each letter of the word into its corresponding phonetic code word.
4. Displays the list of phonetic code words for the inputted word.

## Features
- Supports any word input by the user.
- Handles both uppercase and lowercase input by converting the input to uppercase.
- Utilizes the NATO phonetic alphabet for each letter of the English alphabet.

## Requirements
- Python 3.11
- pandas library

You can install pandas by running the following command:
```bash
pip install pandas
```
## Code Breakdown
1. **Loading the CSV file:**\
    The CSV file [nato_phonetic_alphabet.csv](./nato_phonetic_alphabet.csv)
 is read into a Pandas DataFrame.

2. **Dictionary Creation:**\
   The dictionary nato_dict is created using a dictionary comprehension. The keys are the letters from the "letter" column, and the values are the corresponding phonetic codes from the "code" column in the DataFrame.

3. **User Input:**\
   The program prompts the user to input a word, which is then converted to uppercase to handle case insensitivity.

4. **Phonetic Conversion:**\
   The user’s word is converted into a list of phonetic code words using the constructed dictionary.

## Example Usage
```
Enter a word: Hello
['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
```
## Notes
- The CSV file [nato_phonetic_alphabet.csv](./nato_phonetic_alphabet.csv)
 should contain the alphabet and phonetic codes in the following format:
```
letter, code
A, Alfa
B, Bravo
...
```
## Future Improvements
- Error handling for invalid characters in user input (non-alphabetic characters).
- Adding functionality to handle multiple words or phrases input by the user.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
Darshan Nayee
