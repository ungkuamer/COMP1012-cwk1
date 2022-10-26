"""
Introduction to Programming: Coursework 1
Please write your name
@author: Ungku Amer Iskandar

"""

# Reminder: You are not allowed to import any modules.


def wordsearch(puzzle: list, wordlist: list) -> None: # checked
    if (valid_puzzle(puzzle) == True) and (valid_wordlist(wordlist) == True):
        print('OK') # replace with coloured display when done
    else:
        print('ValueError, invalid puzzle or wordlist')


def valid_puzzle(puzzle: list) -> bool: # checked
    flag = True
    count = 0

    while (flag == True) and (count < len(puzzle)):
        if len(puzzle[count]) != len(puzzle[0]):
            flag = False
        count += 1
    return flag 


def valid_wordlist(wordlist: list) -> bool: # checked
    flag = True
    count = 0

    while (flag == True) and (count <= len(wordlist)):
        if type(wordlist[count-1]) != str:
            flag = False
        count += 1
    return flag


def get_positions(puzzle: list, word: str) -> list:  # checked
    word = word.upper()
    start_pos = []
    first_char = word[0]
    for i in range(0, len(puzzle)):
        for j in range(0, len(puzzle[i])):
            if (puzzle[i][j] == first_char):
                start_pos.append([i,j])
    # Check all starting positions for word
    for p in start_pos:
        if check_start(puzzle, word, p) != None:
            return check_start(puzzle, word, p)
    # Word not found
    print("'{}' Not found".format(word))


def basic_display(grid: list) -> None:  # checked
    current_row = []

    for i in range(0, len(grid)):
        current_row = [x for x in grid[i]]

        print(" "+current_row[0].upper()+" ", end="")
        for j in range(1, len(current_row)-1):
            print(current_row[j].upper()+" ", end="")
        print(current_row[len(current_row)-1].upper())


def coloured_display(grid: list, positions: list) -> None:
    new_pos = []
    for i in range(len(positions)):
        for j in range(len(positions[i])):
            new_pos.append(positions[i][j])
    
    positions = sorted(new_pos , key=lambda k: [k[0], k[1]])

    for x in range(0, len(grid)):
        line = ''
        for y in range(0, len(grid[x])):
            is_pos = False

            for z in positions:
                if (z[0] == x) and (z[1] == y):
                    is_pos = True
            if is_pos:
                line = line + "\033[42m{}\033[0m ".format(grid[x][y])
            else:
                line = line + grid[x][y] + " "
        print(line)
    print('')

    print('')
    print(positions)



        
##### custom function ######

def check_dir (puzzle, word, start_pos, dir): # checked
    """Checks if the word is in a direction dir from the start_pos position in the puzzle. Returns True and prints result if word found"""
    found_chars = [word[0]] # Characters found in direction. Already found the first character
    current_pos = start_pos # Position we are looking at
    pos = [start_pos] # Positions we have looked at
    while (chars_match(found_chars, word)):
        if (len(found_chars) == len(word)):
            coordinates = []
            for x in range(0, len(puzzle)):
                for y in range(0, len(puzzle[x])):
                    is_pos = False
                    for z in pos:
                        if (z[0] == x) and (z[1] == y):
                            is_pos = True
                    if (is_pos):
                        coordinates.append((y, x))
            return coordinates

        # Have not found enough letters so look at the next one
        current_pos = [current_pos[0] + dir[0], current_pos[1] + dir[1]]
        pos.append(current_pos)
        if (is_valid_index(puzzle, current_pos[0], current_pos[1])):
            found_chars.append(puzzle[current_pos[0]][current_pos[1]])
        else:
            # Reached edge of puzzle and not found word
            return

def check_start (puzzle, word, start_pos): # checked
    """Checks if the word starts at the startPos. Returns True if word found"""
    directions = [[-1,1], [0,1], [1,1], [-1,0], [1,0], [-1,-1], [0,-1], [1,-1]]
    # Iterate through all directions and check each for the word
    for d in directions:
        if (check_dir(puzzle, word, start_pos, d)) != None:
            return check_dir(puzzle, word, start_pos, d)

def chars_match (found, word): # checked
    """Checks if the leters found are the start of the word we are looking for"""
    index = 0
    for i in found:
        if (i != word[index]):
            return False
        index += 1
    return True

def is_valid_index (puzzle, line_num, col_num): # checked
    """Checks if the provided line number and column number are valid"""
    if ((line_num >= 0) and (line_num < len(puzzle))):
        if ((col_num >= 0) and (col_num < len(puzzle[line_num]))):
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
    # test_valid_puzzle()
    # test_valid_wordlist()
    # test_basic_display()

    # full solution
    # test_coloured_display()
    # test_get_positions()
    # test_wordsearch()

