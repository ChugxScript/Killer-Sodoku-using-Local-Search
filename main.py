import random

def generate_board():
    return [[0 for _ in range(4)] for _ in range(4)]

def is_valid(board, row, col, num, cage_sum, cells):
    # Check if the number is not present in the same row
    if num in board[row]:
        print(f"Number {num} already present in row {row}")
        return False
    
    # Check if the number is not present in the same column
    if num in [board[i][col] for i in range(4)]:
        print(f"Number {num} already present in column {col}")
        return False
    
    # Check if the number is not present in the same 2x2 subgrid
    start_row, start_col = 2 * (row // 2), 2 * (col // 2)
    for i in range(start_row, start_row + 2):
        for j in range(start_col, start_col + 2):
            if board[i][j] == num:
                print(f"Number {num} already present in subgrid starting at ({start_row},{start_col})")
                return False
    
    # check if the number in cages is = cage_sum
    total = 0
    for cell in cells:
        row, col = cell
        total += board[row][col]
    if total != int(cage_sum):
        print(f"Invalid cage: sum {total} does not match expected sum {cage_sum}")
        return False
    
    return True

def first_choice_algorithm(board, cages):
    for cage in cages:
        cage_sum, cells = cage
        for cell in cells:
            row, col = cell
            for num in range(1, 5):
                if is_valid(board, row, col, num, cage_sum, cells):
                    board[row][col] = num
                    if first_choice_algorithm(board, cages):
                        return True
            return False
    return True

def get_cage_input(board):
    available_coordinates = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    while True:
        print("Available coordinates:", available_coordinates)
        cage_input = input("Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): ")
        cells = [tuple(map(int, cell.split(','))) for cell in cage_input.split()]
        valid_cells = True
        print(f"---[print] cells: {cells}\n")
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
            print("Invalid input. Sum must be a positive integer.")
        else:
            if (int(cage_sum) > 0 and int(cage_sum) >= len(cells) and int(cage_sum) <= (len(cells) * 4)):
                return check_cage_sum(board, cells, cage_sum)
            else:
                print("\nInvalid input. Sum must be a align with the length of the cage.")
                print(f"Available cage sum is from [{len(cells)}] to [{len(cells) * 4}]\n")

def check_cage_sum(board, cells, cage_sum):
    while True:
        generate_cell_num(board, cells)
        # check cage sum
        total = 0
        for cell in cells:
            row, col = cell
            total += board[row][col]
        if total == int(cage_sum):
            return int(cage_sum)

def generate_cell_num(board, cells):
    for cell in cells:
        row, col = cell
        num = random.randint(1, 4)
        board[row][col] = num

def print_boxes_layout(board):
    print("Boxes Layout:")
    for i in range(4):
        for j in range(4):
            print("+-", end="")
        print("+")
        for j in range(4):
            if board[i][j] == 0:
                print("| ", end="")
            else:
                print(f"|{board[i][j]}", end="")
        print("|")

def main():
    board = generate_board()
    print("Welcome to 4x4 Killer Sudoku!")
    print("Please enter the cages:")
    print(f"\n---[print] board: {board}")
    print_boxes_layout(board)
    cages = []
    while any(0 in row for row in board):
        print(f"\nCage {len(cages) + 1}:")
        cells = get_cage_input(board)
        cage_sum = get_cage_sum(board, cells)
        cages.append((cage_sum, cells))
        
        print("Updated board:")
        print_boxes_layout(board)

    print(f"\n---[print] board: {board}")
    print(f"---[print] cages: {cages}\n")
    success = first_choice_algorithm(board, cages)
    if success:
        print("\nSolution found:")
        print_boxes_layout(board)
    else:
        print("\nNo solution found.")

if __name__ == "__main__":
    main()
