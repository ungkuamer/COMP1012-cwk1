
puzzle = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']


found = False
coordinates = []
word = 'DNUO'
count = 0

max_x = len(puzzle[0])
max_y = len(puzzle)

while (found == False) and (count != max_y): # search through horizontal-normal
    found_status = puzzle[count].find(word)
    if found_status > -1:
        for j in range(len(word)): # i referes to x-coordinate
            coordinates.append((j,i))
        break
        found = True
    count += 1

count = 0
print('Pass test 1')

while (found == False) and (count != max_y): # search through horizontal-flipped
    current_line = puzzle[count]
    flipped_line = current_line[::-1]
    print(flipped_line)
    found_status = flipped_line.find(word)
    if found_status > -1:
        for i in range(len(word)):
            new_x = max_x - found_status - 1 - i
            coordinates.append((new_x, count))
        break
        found = True
    count += 1

print(coordinates)



