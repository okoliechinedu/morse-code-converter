def morse_code_converter(given_word):
    input_morse_code = []
    for string in given_word:
        if string in morse_dict:    # word to morse code
            input_morse_code.append(morse_dict[string])
    print(' '.join(input_morse_code))


alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
             "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
              "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
              "..-", "...-", ".--", "-..-", "-.--", "--.."]


morse_dict = {key: value for (key, value) in zip(alphabets, morse_code)}


user_input = input("Enter a word or sentence: ").lower()
morse_code_converter(user_input)









