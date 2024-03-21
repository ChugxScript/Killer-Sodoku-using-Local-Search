from itertools import combinations
import random
cages = []

def generate_board():
    return [[0 for _ in range(4)] for _ in range(4)]

def print_board(board, cages):
    for i in range(4):
        print(f"    [{i}]", end="   ")
    print()

    for i in range(4):
        for j in range(4):
            print("+---------", end="")
        print("+")

        for j in range(4):
            cell = board[i][j]
            cage_sum, cage_grp = check_cagesum(cages, (i, j))
            print(f"| ({cage_grp}|{cage_sum}) {cell} ", end="")
        print(f"| [{i}]")

    for j in range(4):
        print("+---------", end="")
    print("+")

def check_cagesum(cages, coord):
    for i, (cage_sum, cells) in enumerate(cages):
        if coord in cells:
            return cage_sum, i
    return 0, 0

def available_coords():
    all_coords = set((i, j) for i in range(4) for j in range(4))
    user_coords = set(coords for _, cage in cages for coords in cage)
    avail_coords = all_coords - user_coords
    return sorted(list(avail_coords))

def get_cage_input():
    while True:
        available_coordinates = available_coords()
        print("Available coordinates: ", available_coordinates)
        cage_input = input("Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): ")

        if not all(char.isdigit() or char == ',' or char.isspace() for char in cage_input):
            print("[Error] Invalid input.")
            print("   - Please enter only numbers separated by commas and spaces.\n\n")
        else:
            valid_cells = True
            cells = [tuple(map(int, cell.split(','))) for cell in cage_input.split()]
            for cell in cells:
                if cell not in available_coordinates:
                    print(f"[Error] cell:{cell} already assigned to another cage.\n\n")
                    valid_cells = False
                    break
            if valid_cells:
                return cells

def available_cage_sum(cell_len):
    numbers = [1, 2, 3, 4]
    cage_sums = set()
    for combi in list(combinations(numbers, cell_len)):
        cage_sums.add(sum(combi))
    
    return sorted(list(cage_sums))

def get_cage_sum(cell_len):
    while True:
        available_cagesum = available_cage_sum(cell_len)
        print("Available cage sum: ", available_cagesum)
        user_cage_sum = input("Enter the sum for this cage: ")
        if not user_cage_sum.isdigit():
            print(f"[Error] Cage sum:[{user_cage_sum}] is not integer. Try again.\n\n")
        elif not user_cage_sum not in available_cagesum:
            print(f"[Error] Cage sum:[{user_cage_sum}] is not in available cage sums. Try again.\n\n")
        else:
            return int(user_cage_sum)

def generate_cellnum(cages):
    while True:
        for cage_sum, cage in cages:
            rand_num = generate_randnum(cage_sum, len(cage) - 1)
            for x, y in cage:
                board[x][y] = rand_num.pop()
        
        board_errors = check_errors(board, "generate")
        if board_errors != 0:
            for _, cells in cages:
                i, j = random.choice(cells)
                clap_i, clap_j = random.choice(cells)
                board[i][j], board[clap_i][clap_j] = board[clap_i][clap_j], board[i][j]
        
            check_board_error = check_errors(board, "generate")
            if check_board_error >= board_errors:
                for _, cells in cages:
                    i, j = random.choice(cells)
                    clap_i, clap_j = random.choice(cells)
                    board[i][j], board[clap_i][clap_j] = board[clap_i][clap_j], board[i][j]
        else:
            return True

        
def generate_randnum(cage_sum, cage_len):
    while True:
        init_num = [random.randint(1, 4) for _ in range(cage_len)]
        rand_num = cage_sum - sum(init_num)
        gen_nums = set(init_num + [rand_num])
        if 0 < rand_num <= 4 and len(gen_nums) == (cage_len + 1):
            break

    init_num.append(rand_num)
    random.shuffle(init_num)
    return init_num

def check_errors(board, mode):
    row_errors = check_row_errors(board, mode)
    col_errors = check_col_errors(board, mode)
    subgrid_errors = check_subgrid_errors(board, mode)

    return (row_errors + col_errors + subgrid_errors)

def check_row_errors(board, mode):
    duplicates = 0
    for row in board:
        row_nums = set()
        for num in row:
            if num == 0:
                if mode == "generate":
                    continue
                elif mode == "back_jump":
                    duplicates += 1
            elif num in row_nums:
                duplicates += 1
            else:
                row_nums.add(num)
    return duplicates

def check_col_errors(board, mode):
    duplicates = 0
    for col in range(len(board[0])):
        col_nums = set()
        for row in board:
            num = row[col]
            if num == 0:
                if mode == "generate":
                    continue
                elif mode == "back_jump":
                    duplicates += 1
            elif num in col_nums:
                duplicates += 1
            else:
                col_nums.add(num)
    return duplicates

def check_subgrid_errors(board, mode):
    duplicate = 0
    subgrid = 2

    for row in range(0, len(board), subgrid):
        for col in range(0, len(board[0]), subgrid):
            subgrid_nums = set()

            for sub_row in range(row, row + subgrid):
                for sub_col in range(col, col + subgrid):
                    num = board[sub_row][sub_col]
                    if num == 0:
                        if mode == "generate":
                            continue
                        elif mode == "back_jump":
                            duplicate += 1
                    elif num in subgrid_nums:
                        duplicate += 1
                    else:
                        subgrid_nums.add(num)
    return duplicate

def back_jump(board):
    while True:
        board_errors = check_errors(board, "back_jump")
        if board_errors != 0:
            for _, cells in cages:
                i, j = random.choice(cells)
                clap_i, clap_j = random.choice(cells)
                board[i][j], board[clap_i][clap_j] = board[clap_i][clap_j], board[i][j]

            check_board_error = check_errors(board, "back_jump")
            if check_board_error >= board_errors:
                for _, cells in cages:
                    i, j = random.choice(cells)
                    clap_i, clap_j = random.choice(cells)
                    board[i][j], board[clap_i][clap_j] = board[clap_i][clap_j], board[i][j]
        else:
            print("!! SOLUTION FOUND !!")
            print_board(board, cages)
            break
        
if __name__ == "__main__":
    board = generate_board()
    print("!! WELCOME TO KILLER SUDOKU !!")
    print("-----------------------------------")
    print("STARTING TABLE: ")
    while available_coords():
        print_board(board, cages)
        cells = get_cage_input()
        cells_sum = get_cage_sum(len(cells))
        cages.append((cells_sum, cells))
        if generate_cellnum(cages):
            print("\nUPDATED BOARD:")
    
    back_jump(board)

    print("-----------------------------------")
    print("MACHINE PROBLEM 3")
    print("4X4 KILLER SUDOKU USING BACK JUMPING")
    print("BY: ANDREW OLOROSO")
    print("GITHUB REPO: https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/tree/main/back_jumping")
    print("-----------------------------------")