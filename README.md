## Morse Code Converter

This code is a simple Morse code converter that takes a word or sentence as input and converts it into Morse code. The program uses a dictionary to map each alphabet to its corresponding Morse code representation.

### Usage

1. Run the code using a Python interpreter.
2. Enter a word or sentence when prompted: `Enter a word or sentence: <your_input>`.
3. The program will convert the input into Morse code and display the result.

### Code Explanation

The code consists of the following components:

1. `morse_code_converter(given_word)`: This function takes a word or sentence as input (`given_word`) and converts it into Morse code. It iterates through each character in the given word and checks if it exists in the `morse_dict` dictionary. If a match is found, the corresponding Morse code is appended to the `input_morse_code` list. Finally, the Morse code is printed by joining the elements of the `input_morse_code` list with a space delimiter.

2. `alphabets` and `morse_code`: These lists store the alphabets and their corresponding Morse code representations, respectively.

3. `morse_dict`: This dictionary is created using dictionary comprehension to map each alphabet to its corresponding Morse code.

4. `user_input`: This variable captures the word or sentence input provided by the user.

5. The `morse_code_converter(user_input)` line invokes the `morse_code_converter` function with the user's input to convert it into Morse code.

Feel free to modify the code according to your requirements and explore different functionalities related to Morse code conversion.
