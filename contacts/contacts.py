# https://www.hackerrank.com/challenges/contacts/problem
#!/bin/python3
import os


CONTACTS = list()
RESULTS = list()


def add(name):
    CONTACTS.append(name)


def find(name):
    n = 0
    for contact in CONTACTS:
        if contact.startswith(name):
            n += 1
    RESULTS.append(n)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    queries_rows = int(input())

    comands = {
        "add": add,
        "find": find
    }

    for _ in range(queries_rows):
        comand, name = input().rstrip().split()
        comands[comand](name)

    fptr.write('\n'.join(map(str, RESULTS)))
    fptr.close()
