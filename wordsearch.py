"""
Introduction to Programming: Coursework 1
Please write your name
@author: Ungku Amer Iskandar

"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None: 
    # delete pass to write your code
    pass


def valid_puzzle(puzzle: list) -> bool: # to be checked
    flag = True
    count = 0

    while (flag == True) and (count <= len(puzzle)):
        if len(puzzle[i]) != len(puzzle[0]):
            flag = False
        count += 1
    return flag 

def valid_wordlist(wordlist: list) -> bool: # to be checked
    flag = True
    count = 0

    while (flag == True) and (count <= len(puzzle)):
        if type(puzzle[count]) != str:
            flag = False
        count += 1
    return Flag

def get_positions(puzzle: list, word: str) -> list: # to be checked
    found_chars = [word[0]]
    current_pos = start_pos
    pos = [start_pos]

    while chars_match(found_chars, word):

        if len(found_chars) == len(word):
            coordinates = []
            for x in range(0, len(puzzle)):
                for y in range(0, len(puzzle[x])):
                    is_pos = False
                    for z in pos:
                        if (z[0] == x) and (z[1] == y):
                            is_pos = True
                    if is_pos == True:
                        coordinates.append((x, y))
            print(coordinates)
            return True;

        current_pos = [current_pos[0] + dir[0], current_pos[1] + dir[1]]
        pos.append(current_pos)

        if is_valid_index(puzzle, current_pos[0], current_pos[1]):
            found_chars.append(puzzle[current_pos[0]][current_pos[1]])
        else:
            return

def basic_display(grid: list) -> None:  # checked
    current_row = []

    for i in range(0, len(grid)):
        current_row = [x for x in grid[i]]

        print(" "+current_row[0]+" ", end="")
        for j in range(1, len(current_row)-1):
            print(current_row[j]+" ", end="")
        print(current_row[len(current_row)-1])


def coloured_display(grid: list, positions: list) -> None:
    # delete pass to write your code
    pass

# start of custom function

def check_start(puzzle, word, start_pos):
    # check if the word starts at start_pos
    directions = [[-1,1], [0,1], [1,1], [-1,0], [1,0], [-1,-1], [0,-1], [1,-1]]
    # loop through all direction to find the word
    for d in directions:
        if (check_dir(puzzle, word, start_pos, d)):
            return True

def find_word(puzzle, word):
    start_pos = []
    first_char = word[0]

    for i in range(0, len(puzzle)):
        for j in range(0, lne(puzzle[i])):
            if puzzle[i][j] == first_char:
                start_pos.append([i,j])

    for k in start_pos:
        if check_start(puzzle, word, k):
            return
    print("'{}' Not found ".format(word))

def chars_match(found, word):
    count = 0

    for i in found:
        if i != word[count]:
            return False
        count += 1
    return True

def is_valid_index(puzzle, line, colum):
    if (line >= 0) and (line < len(puzzle)):
        if (column >= 0) and (column < len(puzzle[line])):
            return True
    return False


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
