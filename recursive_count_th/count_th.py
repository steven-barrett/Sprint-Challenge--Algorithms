'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    testCase = "th"
    occurences = countInString(word, testCase)
    return occurences
    # print("Times in the string: ", occurences)  # Testing code


def countInString(word, testCase):

    n1 = len(word)
    n2 = len(testCase)

    # Base-case
    if (n1 == 0 or n1 < n2):
        return 0

    # Checking if the first
    # substring matches
    if (word[0: n2] == testCase):
        return countInString(word[n2 - 1:],
                             testCase) + 1

    # Otherwise return the count
    return countInString(word[n2 - 1:],
                         testCase)


# testWord = "abcthefththghith"
# count_th(testWord)
