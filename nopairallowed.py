#!/bin/python3

def minimalOperations(words):
    # Write your code here
    resp = list()
    for word in words:
        changes = 0

        iter_word = iter(word)
        left_char = next(iter_word)
        right_char = next(iter_word)

        while True:
            if left_char == right_char:
                changes += 1
                right_char = next(iter_word, False)

            left_char = right_char
            right_char = next(iter_word, False)

            if not right_char:
                break

        resp.append(changes)
    return resp


if __name__ == '__main__':
    for words in [["add", "boook", "break"]]:
        res = minimalOperations(words)
        print(res)
