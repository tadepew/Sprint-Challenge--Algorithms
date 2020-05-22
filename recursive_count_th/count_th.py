'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # base case
    # if "th" is not in word (handles empty word too apparently) stop calling recursion
    if "th" not in word:
        return 0

    # if 'th' is in word, set new word index to occurence of th and add 2 so the new index is now the letter past the 'th'
    if "th" in word:
        index = word.find("th")
        index += 2

    # add 1 to return each time count_th was called to count how many times th occurred
    return 1 + count_th(word[index:])
