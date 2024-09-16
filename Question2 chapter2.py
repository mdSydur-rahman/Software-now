def separate_and_convert(s):
    # Separate the numbers and letters into two substrings
    number_substring = ''.join([char for char in s if char.isdigit()])
    letter_substring = ''.join([char for char in s if char.isalpha()])

    # Convert even numbers to ASCII code decimal values
    even_numbers = [int(num) for num in number_substring if int(num) % 2 == 0]
    even_numbers_ascii = [ord(str(num)) for num in even_numbers]

    # Convert uppercase letters to ASCII code decimal values
    uppercase_letters = [char for char in letter_substring if char.isupper()]
    uppercase_letters_ascii = [ord(char) for char in uppercase_letters]

    # Print the results
    print(f"Number substring: {number_substring}")
    print(f"Letter substring: {letter_substring}")
    print(f"Even numbers: {even_numbers}")
    print(f"ASCII codes for even numbers: {even_numbers_ascii}")
    print(f"Uppercase letters: {uppercase_letters}")
    print(f"ASCII codes for uppercase letters: {uppercase_letters_ascii}")

# Example scenario
s = '56aAww1984sktr235270aYmn145ss785fsq31D0'
separate_and_convert(s)
def decipher_cryptogram(cipher_text, shift):
    deciphered_text = ""

    # Loop through each character in the cipher text
    for char in cipher_text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Shift character back by the given shift value
            deciphered_char = chr((ord(char) - base - shift) % 26 + base)
            deciphered_text += deciphered_char
        else:
            # Non-alphabet characters remain unchanged
            deciphered_text += char

    return deciphered_text

def find_shift_key(cipher_text):
    # Try all possible shift keys from 1 to 25
    for shift in range(1, 26):
        possible_decipher = decipher_cryptogram(cipher_text, shift)
        print(f"Shift {shift}: {possible_decipher}")

# Example cipher text
cipher_text = "VZ FRYSVFUV ZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXRF ZVFGNXRFF V NZ BHG BS PBAGEBY..."
find_shift_key(cipher_text)
