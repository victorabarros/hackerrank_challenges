#!/bin/python3


# Complete the gameOfThrones function below.
def gameOfThrones(word):
    isPalindromic(word)
    pass


def isPalindromic(word: str) -> bool:
    max = len(word)
    idx = 1

    for ch in word:
        if ch != word[max - idx]:
            return False
        idx += 1
    return True


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # s = input()
    # result = gameOfThrones(s)
    # fptr.write(result + '\n')
    # fptr.close()

    for word in ["aaabbbb", "cdefghmnopqrstuvw", "cdcdcdcdeeeef"]:
        print(gameOfThrones(word))
