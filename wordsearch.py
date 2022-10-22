"""
Introduction to Programming: Coursework 1
Please write your name
@author: Ungku Amer Iskandar

"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None:
    # delete pass to write your code
    pass


def valid_puzzle(puzzle: list) -> bool:
    flag = True
    count = 0

    while (flag == True) and (count <= len(puzzle)):
        if len(puzzle[i]) != len(puzzle[0]):
            flag == False
        count += 1

    return Flag  # done (tbc)

def valid_wordlist(wordlist: list) -> bool:
    flag = True
    count = 0

    while (flag == True) and (count <= len(puzzle)):
        if type(puzzle[count]) != str:
            flag = False
        count += 1

    return Flag  # done (tbc)

def get_positions(puzzle: list, word: str) -> list:

    flag = False
    x = 0
    y = 0

    max_x = len(puzzle[0])
    max_y = len(puzzle)
    word_len = len(word)

    index_position = [" "]*word_len

    while (y <= max_y) and (flag == False):
        if current_char == word[0]:
            if (x=0) and (y=0):
                for i in range(3):



def basic_display(grid: list) -> None:  # done, checked
    current_row = []

    for i in range(len(grid)):
        current_row = [x for x in grid[i]]

        print(" "+current_row[0]+" ", end="")
        for j in range(1, len(current_row)-1):
            print(current_row[j]+" ", end="")
        print(current_row[len(current_row)-1])


def coloured_display(grid: list, positions: list) -> None:
    # delete pass to write your code
    pass


# =============================================================================
# Do not remove the followings. To test your functions
# =============================================================================


def test_valid_wordlist():
    """
    Test function valid_wordlist()
    """
    good_wordlist = ["scalar", "tray", "blew", "sevruc", "testing"]
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    bad_wordlist2 = ["scalar", "tray", "blew", "sevruc", 59]

    print("wordlist is", valid_wordlist(good_wordlist))
    print("wordlist is", valid_wordlist(good_wordlist2))
    print("wordlist is", valid_wordlist(bad_wordlist2))


def test_valid_puzzle():
    good_puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle1 = ['RUNAROUNDDL', 'EDCITOAHC', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    bad_puzzle2 = ['RUNAROUNDDL', ['EDCITOAHCYV'], ('ZYUWSWEDZYA'),
                   'AKOTCONVOYV', 'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL',
                   'ISTREWZLCGY', 'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

    print("puzzle is", valid_puzzle(good_puzzle))
    print("puzzle is", valid_puzzle(bad_puzzle1))
    print("puzzle is", valid_puzzle(bad_puzzle2))


def test_basic_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    basic_display(puzzle1)
    basic_display([['a', 'b', 'c', 'd', 'e'], ['h', 'l', 'j', 'k', 'l']])


def test_get_positions():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    get_positions(puzzle1, "TESTING")
    print(get_positions(puzzle1, "TRAY"))


def test_coloured_display():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    final_list = []
    for word in good_wordlist2:
        temp = get_positions(puzzle1, word)
        if temp is not None:
            final_list.append(temp)
    coloured_display(puzzle1, final_list)


def test_wordsearch():
    puzzle1 = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
               'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
               'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']
    good_wordlist2 = ["scalar", "tray", "blew", "sevruc"]
    wordsearch(puzzle1, good_wordlist2)


if __name__ == "__main__":
    # uncomment the test function individually
    # basic solution
    test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    # test_get_positions()
    # test_wordsearch()
