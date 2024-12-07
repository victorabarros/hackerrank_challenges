#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    import string
    import math
    output = ''

    for character in s:
        # index = string.ascii_letters.find(character)

        # if index == -1:
        #     output += character
        #     continue

        collection = string.ascii_lowercase
        index = string.ascii_lowercase.find(character)
        if index == -1:
            collection = string.ascii_uppercase
            index = string.ascii_uppercase.find(character)
            if index == -1:
                output += character
                continue


        new_index = math.fmod(index + k, len(collection))
        output += collection[int(new_index)]

    return output

if __name__ == '__main__':
    input_string = 'middle-Outz'

    print(input_string)
    print(caesarCipher(input_string, 2)) # okffng-Qwvb
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = input()

    # k = int(input().strip())

    # result = caesarCipher(s, k)

    # fptr.write(result + '\n')

    # fptr.close()
