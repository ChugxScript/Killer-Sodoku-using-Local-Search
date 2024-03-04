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
        print("\n\nUpdated board:")
        print_boxes_layout(board)

def generate_cell_num(board, cells, cage_sum):
    global cages
    count = 1
    track_cage = 0
    cages_length = len(cages) - 1
    numbers = [1, 2, 3, 4]

    while True:
        # Generate numbers for the cage
        for perm in permutations(numbers, len(cells)):
            if sum(perm) == cage_sum:
                for idx, cell in enumerate(cells):
                    row, col = cell
                    board[row][col] = perm[idx]

                row_errors, col_errors, duplicates = check_cage(board)
                if sum(row_errors) == 0 and sum(col_errors) == 0 and not duplicates:
                    return True
        
        for cell in cells:
            row, col = cell
            board[row][col] = 0
        
        if track_cage > cages_length:
            return False

        check_cage_sum, check_cells = cages[cages_length - track_cage]
        perm_length = sum(1 for perm in permutations(numbers, len(check_cells)) if sum(perm) == check_cage_sum)

        track = 0
        for perm in permutations(numbers, len(check_cells)):
            if sum(perm) == check_cage_sum and track < count:
                for idx, cell in enumerate(check_cells):
                    row, col = cell
                    board[row][col] = perm[idx]
                track += 1

        row_errors, col_errors, duplicates = check_cage(board)
        if sum(row_errors) == 0 and sum(col_errors) == 0 and not duplicates:
            if count > perm_length:
                track_cage += 1
            count += 1
        else:
            return False

def is_to_sum(board, cells, cage_sum):
    total = 0
    for cell in cells:
        row, col = cell
        total += board[row][col]
    if total == cage_sum:
        return True
    return False

def check_cage(board):
    n = len(board)
    row_errors = [0] * n
    col_errors = [0] * n
    
    # Count errors in each row and column
    for i in range(n):
        row_nums = set()
        col_nums = set()
        for j in range(n):
            if board[i][j] != 0:
                if board[i][j] in row_nums:
                    row_errors[i] += 1
                else:
                    row_nums.add(board[i][j])
            
            if board[j][i] != 0:
                if board[j][i] in col_nums:
                    col_errors[i] += 1
                else:
                    col_nums.add(board[j][i])
    
    # dups
    duplicates = {}
    # Iterate through each 2x2 subgrid
    for i in range(0, len(board), 2):
        for j in range(0, len(board[0]), 2):
            coord = {}
            subgrid_values = set()
            for x in range(i, i + 2):
                for y in range(j, j + 2):
                    cell_value = board[x][y]
                    if cell_value != 0:
                        if cell_value in subgrid_values:
                            if cell_value in duplicates:
                                duplicates[cell_value].append((x, y))
                            else:
                                duplicates[cell_value] = [(x, y), coord[cell_value]]
                        else:
                            coord[cell_value] = (x, y)
                            subgrid_values.add(cell_value)

    return row_errors, col_errors, duplicates

def solve(board):
    global cages
    track_cage = 0
    count = 1
    cages_length = len(cages) - 1
    numbers = [1, 2, 3, 4]

    while True:
        cage_sum, cells = cages[cages_length]

        for perm in permutations(numbers, len(cells)):
            if sum(perm) == cage_sum:
                for idx, cell in enumerate(cells):
                    row, col = cell
                    board[row][col] = perm[idx]
            
                row_errors, col_errors = print_error_counts(board)
                duplicates = find_duplicate_coordinates(board)

                if sum(row_errors) == 0 and sum(col_errors) == 0 and not duplicates:
                    return True

        for cell in cells:
            row, col = cell
            board[row][col] = 0

        if track_cage > cages_length:
            return False
        
        check_cage_sum, check_cells = cages[cages_length - track_cage]
        perm_length = sum(1 for perm in permutations(numbers, len(cells)) if sum(perm) == cage_sum)
        
        track = 0
        for perm in permutations(numbers, len(check_cells)):
            if sum(perm) == check_cage_sum and track < count:
                for idx, cell in enumerate(check_cells):
                    row, col = cell
                    board[row][col] = perm[idx]
                track += 1

        row_errors, col_errors = print_error_counts(board)
        duplicates = find_duplicate_coordinates(board)
        if sum(row_errors) == 0 and sum(col_errors) == 0 and not duplicates:
            if count > perm_length:
                track_cage += 1
            count += 1
        else:
            return False

def print_error_counts(board):
    n = len(board)
    row_errors = [0] * n
    col_errors = [0] * n
    
    # Count errors in each row and column
    for i in range(n):
        row_nums = set()
        col_nums = set()
        for j in range(n):
            if board[i][j] == 0:
                row_errors[i] += 1
            elif board[i][j] in row_nums:
                row_errors[i] += 1
            else:
                row_nums.add(board[i][j])
            
            if board[j][i] == 0:
                col_errors[i] += 1
            elif board[j][i] in col_nums:
                col_errors[i] += 1
            else:
                col_nums.add(board[j][i])
    
    return row_errors, col_errors

def find_duplicate_coordinates(board):
    duplicates = {}

    # Iterate through each 2x2 subgrid
    for i in range(0, len(board), 2):
        for j in range(0, len(board[0]), 2):
            coord = {}
            subgrid_values = set()
            for x in range(i, i + 2):
                for y in range(j, j + 2):
                    cell_value = board[x][y]
                    if cell_value != 0:
                        if cell_value in subgrid_values:
                            if cell_value in duplicates:
                                duplicates[cell_value].append((x, y))
                            else:
                                duplicates[cell_value] = [(x, y), coord[cell_value]]
                        else:
                            coord[cell_value] = (x, y)
                            subgrid_values.add(cell_value)
    
    return duplicates

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
        
        print("\n\nUpdated board:")
        print_boxes_layout(board)
 
    row_errors, col_errors = print_error_counts(board)
    duplicates = find_duplicate_coordinates(board)

    # Check if there are no errors 
    if not row_errors and not col_errors and not duplicates:
        print("\nSolution found:")
        print_boxes_layout(board)
    elif (solve(board)):
        print("\nSolution found:")
        print_boxes_layout(board)
    else:
        print("\nNo solution found.")

if __name__ == "__main__":
    main()