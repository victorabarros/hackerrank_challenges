#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def isPalindrome(input_string):

    for index, character in enumerate(input_string):
        if character != input_string[len(input_string)-1-index]:
            return False
        
        # if index >= len(input_string)/2:
        #     break

    return True

def palindromeIndex(input_string):
    if isPalindrome(input_string):
        return -1

    for index in range(len(input_string)):
        sub_string = input_string[:index] + input_string[index+1:]
        print(index, input_string, sub_string)
        if isPalindrome(sub_string):
            return index

    return -1

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # for q_itr in range(q):
    #     s = input()

    #     result = palindromeIndex(s)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
