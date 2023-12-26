def fizzBuzz(n):
    for ii in range(1, n+1):
        if ii % 15 == 0:
            print("FizzBuzz")
        elif ii % 3 == 0:
            print("Fizz")
        elif ii % 5 == 0:
            print("Buzz")
        else:
            print(ii)


if __name__ == '__main__':
    fizzBuzz(15)
