 
# Exercise 4 : Secret code language
# write a python program to translate a message into secret code language. Use the rules below
# to translate normal English into secret code language.

# encoding :
# if the word contains at least 3 characters, remove the first letter and append it at the end.
# now append 3 random characters at the starting and the end.
# else :
#  simply reverse the string.

# Decoding :
# if the word contains at least 3 characters, reverse it.
# else :
# remove 3 random characters from start and end. Now remove the last letter and append it to the beginning.

# Your program should ask whether to code or decode.

import random
import string

def generate_random_chars(num):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(num))

Encode_Decode = input('Would you like to encode or decode a message? : ').lower()
if Encode_Decode == 'encode':
    print('Encoding : ', '
')
    message = input("enter message to encode : ").lower()
    words = message.split()
    encoded_words = []
    for word in words:
        if len(word) >= 3:
            # Remove the first letter and append it at the end
            modified_word = word[1:] + word[0]
            # Append 3 random characters at the starting and the end
            random_prefix = generate_random_chars(3)
            random_suffix = generate_random_chars(3)
            encoded_word = random_prefix + modified_word + random_suffix
            encoded_words.append(encoded_word)
        else:
            # Simply reverse the string
            encoded_words.append(word[::-1])
    print("Encoded message:", " ".join(encoded_words))

elif Encode_Decode == 'decode':
    print('
', 'Decoding : ', '
')
    encoded_message = input('Enter message to decode : ').lower()
    encoded_words = encoded_message.split()
    decoded_words = []
    for word in encoded_words:
        # Check if the word was encoded from an original word of 3 or more characters
        if len(word) >= 9: # Assuming encoded words from >=3 char words are always >= 9 chars
            # remove 3 random characters from start and end.
            trimmed_word = word[3:-3]
            # Now remove the last letter and append it to the beginning.
            decoded_word = trimmed_word[-1] + trimmed_word[:-1]
            decoded_words.append(decoded_word)
        else:
            # Otherwise, it was originally < 3 characters and was simply reversed
            decoded_words.append(word[::-1])
    print("Decoded message:", " ".join(decoded_words))

else:
    print("Invalid choice. Please enter 'encode' or 'decode'.")
    