'''
Your function should take in a signle parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    prev = word[:1]

    if word == '':
        return 0

    if word[1:2] == 'h' and prev == 't':
        prev = word[:1]
        return 1 + count_th(word[1:])

    prev = word[:1]
    return count_th(word[1:])
