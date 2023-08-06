
## Generate 2 lists one with charaters to be replaced
## And the other with characters that replace

import random
import string
import json

class encryption:

    # I have to replace every char in my input with a coresponding char from key list
    # To decrypt I'll take every char from key and replace it with the coresponding char from message

    def generate_keys(filename):
        chars = " " + string.punctuation + string.digits + string.ascii_letters
        chars = list(chars)
        keys = chars.copy()
        random.shuffle(keys)
        data = {"chars" : chars, "keys": keys}
        with open(filename, 'w') as file:
            json.dump(data, file)

    def encrypt_decrypt(text, first_list, second_list):
            result = ""
            # Find the index of the char to be replaced
            # add the corespoding char to result
            for char in text:
                index = first_list.index(char)
                result += second_list[index]
            return result

    def read_from_json(filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return data['chars'], data['keys']
        


