# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n-1)


def combination(n, k):
    return factorial(n) / (factorial(k) * factorial(n-k))


def sherlockAndAnagrams(query):
    # letters = {ii: 0 for ii in set(query)}
    # for letter in query:
    #     letters[letter] += 1
    # print(letters)
    anagram1 = 0

    for ii, letterii in enumerate(query):
        for jj, letterjj in enumerate(query[ii+1:]):

            if letterii == letterjj:
                anagram1 += 1

    anagram2 = 0
    if len(query) >= 3
    for ii, letterii in enumerate(query):
        for jj, letterjj in enumerate(query[ii+1:]):

            for kk, letterkk in enumerate(query[jj+1:]):
                for ww, letterww in enumerate(query[kk+1:]):
                    print(f"{letterii}{letterjj} == {letterkk}{letterww}")
                    if sorted(f"{letterii}{letterjj}") == \
                       sorted(f"{letterkk}{letterww}"):
                        print(1)
                        anagram2 += 1

    return anagram1 + anagram2


if __name__ == '__main__':
    for query, re in [("mom", 2), ("abba", 4), ("abcd", 0),
                    #   ("ifailuhkqq", 3), ("kkkk", 10), ("cdcd", 5)
                      ]:

        res = sherlockAndAnagrams(query)

        print(res, re)
