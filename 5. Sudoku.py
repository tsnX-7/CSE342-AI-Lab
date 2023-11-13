
def in_row(grid, row, col, num):
    return num in grid[row]

def in_col(grid, row, col, num):
    for i in range(9):
        if grid[i][col]==num:
            return True
    return False

def in_box(grid, row, col, num):
    x = row//3 * 3
    y = col//3 * 3
    for i in range(3):
        for j in range(3):
            if grid[x+i][y+j] == num:
                return True
    return False

def not_zero(grid, row, col, num):
    if grid[row][col] != 0:
        return True
    return False

def is_valid_move(grid, row, col, num):
    if in_row(grid, row, col, num) or in_col(grid, row, col, num) or in_box(grid, row, col, num) or not_zero(grid, row, col, num):
        return False
    return True


def find_empty_cell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(grid):
    row, col = find_empty_cell(grid)
    if row is None:
        return True
    for num in range(1, 10):
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid):
                return True
            grid[row][col] = 0
    return False

def print_sudoku(grid):
    for i in grid:
        print(' '. join(map(str, i)))


grid = [
    [0, 0, 8, 0, 5, 0, 0, 0, 0],
    [1, 0, 0, 9, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 4, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [2, 0, 0, 1, 6, 0, 0, 0, 7],
    [0, 0, 2, 3, 9, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 9],
    [3, 0, 0, 0, 0, 7, 0, 0, 0]
]

if solve_sudoku(grid):
    print_sudoku(grid)
else:
    print('No solution exists for this sudoku formation!')
