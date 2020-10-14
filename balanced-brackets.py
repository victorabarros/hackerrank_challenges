# https://www.hackerrank.com/challenges/balanced-brackets/problem
from copy import copy


OPEN = ["(", "[", "{"]
CLOSE = [")", "]", "}"]

VALIDS = copy(OPEN)
VALIDS.extend(CLOSE)

PAIRS = dict(zip(OPEN, CLOSE))
PAIRS.update(dict(zip(CLOSE, OPEN)))


# Complete the isBalanced function below.
def isBalanced(s) -> bool:
    n = len(s)
    if n % 2 != 0:
        return False

    trail = ""
    for ii, c in enumerate(s):
        if c in OPEN:
            trail += c
        elif c in CLOSE:
            try:
                if not isPair(c, trail[-1]):
                    return False
            except IndexError:
                return False
            trail = trail[:-1]
        else:
            return False

    if trail != "":
        return False

    return True


def isPair(a, b):
    return PAIRS[a] == b


if __name__ == '__main__':
    for s in ["}][}}(}][))]",
              "[](){()}",
              "()",
              "({}([][]))[]()",
              "{)[](}]}]}))}(())(",
              "([[)"]:
        result = "YES" if isBalanced(s) else "NO"
        print(result)
