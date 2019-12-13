'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
import re
def count_th(word):
    if len(word) == 0:
        return 0

    if len(word) == 1:
        return 

    x = re.findall("th", word)
    mid = len(word) // 2
    count_th(word[:mid])
    count_th(word[mid:])
    return len(x)
