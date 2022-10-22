


grid = ['RUNAROUNDDL', 'EDCITOAHCYV', 'ZYUWSWEDZYA', 'AKOTCONVOYV',
                   'LSBOSEVRUCI', 'BOBLLCGLPBD', 'LKTEENAGEDL', 'ISTREWZLCGY',
                   'AURAPLEBAYG', 'RDATYTBIWRA', 'TEYEMROFINU']

#display the grid
current_row = []

for i in range(len(grid)):
    current_row = [x for x in grid[i]]

    print(" "+current_row[0]+" ", end="")
    for j in range(1, len(current_row)-1):
        print(current_row[j]+" ", end="")
    print(current_row[len(current_row)-1])



#finding a certain char in grid assuming its surrounded by 8 char
cor_x = int(input('Enter x: '))
cor_y = int(input('Enter y: '))

row = grid[cor_y]
current_word = row[cor_x]
print(current_word)

row = grid[(cor_y)-1]
print(row[(cor_x)-1]+' ', end='')
print(row[cor_x]+' ', end='')
print(row[(cor_x)+1])

row = grid[cor_y]
print(row[(cor_x)-1]+' ', end='')
print('  ', end='')
print(row[(cor_x)+1])

row = grid[(cor_y)+1]
print(row[(cor_x)-1]+' ', end='')
print(row[cor_x]+' ', end='')
print(row[(cor_x)+1])






