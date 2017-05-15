# Practice Project from Chapter 4: Character Picture Grid

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def printGrid(gridParam):
    x = 0
    y = 0
    while y < len(gridParam[1]):
        column = ''
        while x < len(gridParam):
            column += gridParam[x][y]
            x += 1
        print(column)
        x = 0
        y += 1

printGrid(grid)
