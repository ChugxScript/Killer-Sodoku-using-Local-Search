import random
from itertools import permutations
cages = []

def generate_board():
    return [[0 for _ in range(4)] for _ in range(4)]

def print_boxes_layout(board):
    for i in range(4):
        print(f" [{i}]", end="")
    print()

    for i in range(4):
        for j in range(4):
            print("+---", end="")
        print("+")

        for j in range(4):
            if board[i][j] == 0:
                print("|   ", end="")
            else:
                print(f"| {board[i][j]} ", end="")
        print(f"| [{i}]")

    for j in range(4):
        print("+---", end="")
    print("+")

def get_cage_input(board):
    available_coordinates = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    while True:
        print("Available coordinates:", available_coordinates)
        cage_input = input("Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): ")
        cells = [tuple(map(int, cell.split(','))) for cell in cage_input.split()]
        valid_cells = True
        for cell in cells:
            if cell not in available_coordinates:
                print("Invalid cell coordinates or cell already assigned to another cage. Please choose from available coordinates.")
                valid_cells = False
                break
        if valid_cells:
            return cells

def get_cage_sum(board, cells):
    while True:
        print(f"Available cage sum is from [{len(cells)}] to [{len(cells) * 4}]")
        cage_sum = input("Enter the sum for this cage: ")
        if not cage_sum.isdigit():
            print("\n[! INVALID INPUT !]")
            print("Sum must be a positive integer.\n")
        else:
            if (int(cage_sum) > 0 and int(cage_sum) >= len(cells) and int(cage_sum) <= (len(cells) * 4)):
                if generate_cell_num(board, cells, int(cage_sum)):
                    return int(cage_sum)
                else:
                    print("\n[! ERROR !]")
                    print("No solution found.")
                    print("Cant generate cell numbers base on the sum")
                    print("where row and col are valid.\n")
            else:
                print("\n[! INVALID INPUT !]")
                print("Sum must be a align with the length of the cage.")
                print(f"Available cage sum is from [{len(cells)}] to [{len(cells) * 4}]\n")
        print_boxes_layout(board)

def check_cage_sum(board, cells, cage_sum):
    while True:
        if not generate_cell_num(board, cells):
            return False
        # check cage sum
        total = 0
        for cell in cells:
            row, col = cell
            total += board[row][col]
        if total == int(cage_sum):
            return int(cage_sum)
        print("\n--[print] invalid cage_sum\n")

def generate_cell_num(board, cells, cage_sum):
    global cages
    limit = 0
    limitFlag = 0
    limitEdit = 1
    numbers = [1, 2, 3, 4]

    # Generate all permutations as the limit
    perms = permutations(numbers, len(cells))
    for perm in perms:
        limit += 1

    # generate number on the cage
    while not is_to_sum(board, cells, cage_sum):
        for cell in cells:
            row, col = cell
            num = random.randint(1, 4)
            while not is_valid_cage(board, row, col, num):
                num = random.randint(1, 4)
            board[row][col] = num
        
    return True

def is_valid_cage(board, row, col, num):
    # Check if the number is not present in the same row
    if num in board[row]:
        return False
    
    # Check if the number is not present in the same column
    if num in [board[i][col] for i in range(4)]:
        return False
    
    # Check if the number is not present in the same 2x2 subgrid
    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                return False
    
    return True

def is_to_sum(board, cells, cage_sum):
    total = 0
    for cell in cells:
        row, col = cell
        total += board[row][col]
    if total == cage_sum:
        return True
    return False

def edit_prev_cage(board, cages, cage_idx, cage_sum):
    cage_num, prev_cells = cages
    reset_cells(board, prev_cells)

    limit = 0
    limitFlag = 0
    numbers = [1, 2, 3, 4]

    perms = permutations(numbers, len(prev_cells))
    for perm in perms:
        limit += 1

    while not is_valid_cage(board, prev_cells):

        print(f"\n[edit_prev_cage] tries: [{limitFlag}]")
        print_boxes_layout(board)
        print("\n")

        # check if stuck
        limitFlag += 1
        if (limitFlag > limit + 1):
            return False
            
        # generate number on the cage
        for cell in prev_cells:
            row, col = cell
            num = random.randint(1, 4)
            while not is_to_sum(board, prev_cells, cage_sum):
                num = random.randint(1, 4)
            board[row][col] = num

    print(f"\n[edit_prev_cage] cage_idx: [{cage_idx}] final")
    print_boxes_layout(board)
    print("\n")

    return True

def reset_cells(board, cells):
    for cell in cells:
        row, col = cell
        board[row][col] = 0

def check_board(board):
    for row in board:
        # Check if there are any duplicate numbers in the row
        if len(set(row)) != len(row):
            return False

    for col in range(4):
        column_values = [board[row][col] for row in range(4)]
        # Check if there are any duplicate numbers in the column
        if len(set(column_values)) != len(column_values):
            return False
        
    return True

def main():
    board = generate_board()
    print("Welcome to 4x4 Killer Sudoku!")
    print("Please enter the cages:")
    print_boxes_layout(board)

    global cages
    while any(0 in row for row in board):
        print(f"\nCage {len(cages) + 1}:")
        cells = get_cage_input(board)
        cage_sum = get_cage_sum(board, cells)
        cages.append((cage_sum, cells))
        
        print("Updated board:")
        print_boxes_layout(board)
 
    if (check_board(board)):
        print("\nSolution found:")
        print_boxes_layout(board)
    else:
        print("\nNo solution found.")

if __name__ == "__main__":
    main()