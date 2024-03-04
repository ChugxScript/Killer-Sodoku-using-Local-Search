from itertools import permutations

# Define the numbers
numbers = [1, 2, 3, 4]
perms = permutations(numbers, 3)


print("[permu] 3 numbers whose sum equals 8:")
for perm in perms:
    if sum(perm) == 8:
        print(perm)

# temp = []
# x = 0
# for perm in perms:
#     if sum(perm) == 10 and x < 2:
#         print(perm)
#         temp.append(perm)
#         x += 1

# print(f"temp: {temp}")
# print(f"temp[0]: {temp[0]}")

# tempB = temp[0]
# print(f"tempB[0]: {tempB[0]}")
# print(f"tempB[1]: {tempB[1]}")
# print(f"tempB[2]: {tempB[2]}")
# print(f"tempB[3]: {tempB[3]}")



# ############################################################
# def find_duplicate_coordinates(board):
#     duplicates = {}

#     # Iterate through each 2x2 subgrid
#     for i in range(0, len(board), 2):
#         for j in range(0, len(board[0]), 2):
#             coord = {}
#             subgrid_values = set()
#             for x in range(i, i + 2):
#                 for y in range(j, j + 2):
#                     cell_value = board[x][y]
#                     if cell_value != 0:
#                         if cell_value in subgrid_values:
#                             if cell_value in duplicates:
#                                 duplicates[cell_value].append((x, y))
#                             else:
#                                 duplicates[cell_value] = [(x, y), coord[cell_value]]
#                         else:
#                             coord[cell_value] = (x, y)
#                             subgrid_values.add(cell_value)
    
#     print(f"duplicates: {duplicates}")
#     return duplicates

# def solve(board, duplicates):
#     switch_cage = [0] * len(cages)

#     # check which cage has the most error
#     for cage_index, cage in enumerate(cages):
#         cage_sum, cells = cage

#         for number, coordinates in duplicates.items():
#             for coord in coordinates:
#                 if coord in cells:
#                     switch_cage[cage_index] += 1
    
#     max_errors = max(switch_cage)
#     max_errors_index = switch_cage.index(max_errors)
#     print(f"cages: {cages}")
#     print(f"swict_cage: {switch_cage}")
#     print(f"max_errors: {max_errors}")
#     print("Switching to cage with index:", max_errors_index)

#     switch_cage_sum, switch_cells = cages[max_errors_index]
#     print(f"switch_cage_sum: {switch_cage_sum}")
#     print(f"switch_cells: {switch_cells}")

# # Example usage
# board = [
#     [1, 3, 1, 2],
#     [4, 2, 4, 3],
#     [2, 1, 3, 1],
#     [3, 4, 2, 4]
# ]

# cages = [
#     (8, [(0, 0), (0, 1), (1, 0)]), 
#     (6, [(0, 2), (0, 3), (1, 3)]), 
#     (9, [(2, 0), (3, 0), (3, 1)]), 
#     (7, [(2, 3), (3, 2), (3, 3)]), 
#     (10, [(1, 1), (1, 2), (2, 1), (2, 2)])
# ]

# duplicates = find_duplicate_coordinates(board)
# solve(board, duplicates)






# ###################################################
# from itertools import permutations
# cages = []

# def generate_board():
#     return [[0 for _ in range(4)] for _ in range(4)]

# def print_boxes_layout(board):
#     for i in range(4):
#         print(f" [{i}]", end="")
#     print()

#     for i in range(4):
#         for j in range(4):
#             print("+---", end="")
#         print("+")

#         for j in range(4):
#             if board[i][j] == 0:
#                 print("|   ", end="")
#             else:
#                 print(f"| {board[i][j]} ", end="")
#         print(f"| [{i}]")

#     for j in range(4):
#         print("+---", end="")
#     print("+")

# def get_cage_input(board):
#     available_coordinates = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
#     while True:
#         print("Available coordinates:", available_coordinates)
#         cage_input = input("Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): ")
#         cells = [tuple(map(int, cell.split(','))) for cell in cage_input.split()]
#         valid_cells = True
#         for cell in cells:
#             if cell not in available_coordinates:
#                 print("Invalid cell coordinates or cell already assigned to another cage. Please choose from available coordinates.")
#                 valid_cells = False
#                 break
#         if valid_cells:
#             return cells

# def get_cage_sum(board, cells):
#     while True:
#         print(f"Available cage sum is from [{len(cells)}] to [{len(cells) * 4}]")
#         cage_sum = input("Enter the sum for this cage: ")
#         if not cage_sum.isdigit():
#             print("\n[! INVALID INPUT !]")
#             print("Sum must be a positive integer.\n")
#         else:
#             if (int(cage_sum) > 0 and int(cage_sum) >= len(cells) and int(cage_sum) <= (len(cells) * 4)):
#                 if generate_cell_num(board, cells, int(cage_sum)):
#                     return int(cage_sum)
#                 else:
#                     print("\n[! ERROR !]")
#                     print("No solution found.")
#                     print("Cant generate cell numbers base on the sum")
#                     print("where row and col are valid.\n")
#             else:
#                 print("\n[! INVALID INPUT !]")
#                 print("Sum must be a align with the length of the cage.")
#                 print(f"Available cage sum is from [{len(cells)}] to [{len(cells) * 4}]\n")
#         print("Updated board:")
#         print_boxes_layout(board)

# def generate_cell_num(board, cells, cage_sum):
#     numbers = [1, 2, 3, 4]
#     perms = permutations(numbers, len(cells))

#     # Generate numbers for the cage
#     for perm in perms:
#         if sum(perm) == cage_sum:
#             for idx, cell in enumerate(cells):
#                 row, col = cell
#                 board[row][col] = perm[idx]
#             if is_to_sum(board, cells, cage_sum):
#                 return True

#     return False

# def is_to_sum(board, cells, cage_sum):
#     total = 0
#     for cell in cells:
#         row, col = cell
#         total += board[row][col]
#     if total == cage_sum:
#         return True
#     return False

# def first_choice_algorithm(board):
#     global cages
#     track_cage = [0] * len(cages)
#     x = 0
#     row_errors, col_errors = print_error_counts(board)
#     duplicates = find_duplicate_coordinates(board)

#     # Check if there are no errors 
#     if not row_errors and not col_errors and not duplicates:
#         return True

#     while True:
#         switch_cage = [0] * len(cages)
#         # check which cage has the most error
#         for cage_index, cage in enumerate(cages):
#             cage_sum, cells = cage

#             for number, coordinates in duplicates.items():
#                 for coord in coordinates:
#                     if coord in cells:
#                         switch_cage[cage_index] += 1
#         max_errors = switch_cage.index(max(switch_cage))

#         print(f"\n---[print] cage: {cages}")
#         print(f"---[print] switch_cage: {switch_cage}")
#         print(f"---[print] max_errors: {max_errors}")
#         print(f"---[print] edit cage: {cages[max_errors]}\n")

#         # generate another numbers / switch numbers in the cell in the cage
#         switch_cage_sum, switch_cells = cages[max_errors]
#         numbers = [1, 2, 3, 4]
#         perms = permutations(numbers, len(switch_cells))

#         perm_length = 0
#         for perm in perms:
#             if sum(perm) == switch_cage_sum:
#                 perm_length += 1

#         if track_cage[max_errors] > perm_length:
#             track_cage[max_errors] = 0
#         else:
#             track_cage[max_errors] += 1
#         track = 0

#         perms = permutations(numbers, len(switch_cells))
#         for perm in perms:
#             if sum(perm) == switch_cage_sum and track < track_cage[max_errors]:
#                 print(f"---[print] 2.2 perm: {perm}")
#                 print(f"---[print] track: {track}")
#                 print(f"---[print] track_cage[max_errors]: {track_cage[max_errors]}")
#                 for idx, cell in enumerate(switch_cells):
#                     row, col = cell
#                     board[row][col] = perm[idx]
#                 track += 1
        
#         row_errors, col_errors = print_error_counts(board)
#         duplicates = find_duplicate_coordinates(board)
#         print(f"\n---tries [{x}]---")
#         print_boxes_layout(board)

#         # Check if there are no more errors and break the loop
#         if not row_errors and not col_errors and not duplicates:
#             return True
#         x += 1
    

# def print_error_counts(board):
#     n = len(board)
#     row_errors = [0] * n
#     col_errors = [0] * n
    
#     # Count errors in each row and column
#     for i in range(n):
#         row_nums = set()
#         col_nums = set()
#         for j in range(n):
#             if board[i][j] == 0:
#                 row_errors[i] += 1
#             elif board[i][j] in row_nums:
#                 row_errors[i] += 1
#             else:
#                 row_nums.add(board[i][j])
            
#             if board[j][i] == 0:
#                 col_errors[i] += 1
#             elif board[j][i] in col_nums:
#                 col_errors[i] += 1
#             else:
#                 col_nums.add(board[j][i])
    
#     # Print the error counts for each row and column
#     print("Error counts:")
#     for i in range(n):
#         print(f"Row [{i}] error/s: {row_errors[i]} | Column [{i}] error/s: {col_errors[i]}")
    
#     return row_errors, col_errors

# def find_duplicate_coordinates(board):
#     duplicates = {}

#     # Iterate through each 2x2 subgrid
#     for i in range(0, len(board), 2):
#         for j in range(0, len(board[0]), 2):
#             coord = {}
#             subgrid_values = set()
#             for x in range(i, i + 2):
#                 for y in range(j, j + 2):
#                     cell_value = board[x][y]
#                     if cell_value != 0:
#                         if cell_value in subgrid_values:
#                             if cell_value in duplicates:
#                                 duplicates[cell_value].append((x, y))
#                             else:
#                                 duplicates[cell_value] = [(x, y), coord[cell_value]]
#                         else:
#                             coord[cell_value] = (x, y)
#                             subgrid_values.add(cell_value)
    
#     print(f"duplicates: {duplicates}")
#     return duplicates






# def is_valid_cage(board, row, col, num):
#     # Check if the number is not present in the same row
#     if num in board[row]:
#         return False
    
#     # Check if the number is not present in the same column
#     if num in [board[i][col] for i in range(4)]:
#         return False
    
#     # Check if the number is not present in the same 2x2 subgrid
#     start_row, start_col = 2 * (row // 2), 2 * (col // 2)
#     for i in range(start_row, start_row + 2):
#         for j in range(start_col, start_col + 2):
#             if board[i][j] == num:
#                 return False
    
#     return True

# def check_board(board):
#     for row in board:
#         # Check if there are any duplicate numbers in the row
#         if len(set(row)) != len(row):
#             return False

#     for col in range(4):
#         column_values = [board[row][col] for row in range(4)]
#         # Check if there are any duplicate numbers in the column
#         if len(set(column_values)) != len(column_values):
#             return False
        
#     return True

# def main():
#     board = generate_board()
#     print("Welcome to 4x4 Killer Sudoku!")
#     print("Please enter the cages:")
#     print_boxes_layout(board)

#     global cages
#     while any(0 in row for row in board):
#         print(f"\nCage {len(cages) + 1}:")
#         cells = get_cage_input(board)
#         cage_sum = get_cage_sum(board, cells)
#         cages.append((cage_sum, cells))
        
#         print("Updated board:")
#         print_boxes_layout(board)
 
#     if (first_choice_algorithm(board)):
#         print("\nSolution found:")
#         print_boxes_layout(board)
#     else:
#         print("\nNo solution found.")

# if __name__ == "__main__":
#     main()



# example of being stuck:
# Welcome to 4x4 Killer Sudoku!
# Please enter the cages:
# +-+-+-+-+
# | | | | |
# +-+-+-+-+
# | | | | |
# +-+-+-+-+
# | | | | |
# +-+-+-+-+
# | | | | |

# Cage 1:
# Available coordinates: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
# Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 0,0 0,1 1,0 1,1
# Available cage sum is from [4] to [16]
# Enter the sum for this cage: 10
# Updated board:
# +-+-+-+-+
# |2|1| | |
# +-+-+-+-+
# |3|4| | |
# +-+-+-+-+
# | | | | |
# +-+-+-+-+
# | | | | |

# Cage 2:
# Available coordinates: [(0, 2), (0, 3), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
# Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 0,2 0,3 1,2 1,3
# Available cage sum is from [4] to [16]
# Enter the sum for this cage: 10
# Updated board:
# +-+-+-+-+
# |2|1|4|3|
# +-+-+-+-+
# |3|4|2|1|
# +-+-+-+-+
# | | | | |
# +-+-+-+-+
# | | | | |

# Cage 3:
# Available coordinates: [(2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
# Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 2,0 2,1 3,0 3,1
# Available cage sum is from [4] to [16]
# Enter the sum for this cage: 10
# Updated board:
# +-+-+-+-+
# |2|1|4|3|
# +-+-+-+-+
# |3|4|2|1|
# +-+-+-+-+
# |4|2| | |
# +-+-+-+-+
# |1|3| | |

# Cage 4:
# Available coordinates: [(2, 2), (2, 3), (3, 2), (3, 3)]
# Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 2,2 2,3 3,2 3,3
# Available cage sum is from [4] to [16]
# Enter the sum for this cage: 10
    



            # while not is_valid_cage(board, row, col, num):
            #     print("\n[generate_cell_num] [not valid cage] ")
            #     print(f"cells: [{cells}] | num: [{num}] | attempts: [{limitFlag + 1}]")
            #     print_boxes_layout(board)
            #     print()
                
            #     # check if stuck
            #     limitFlag += 1
            #     if (limitFlag > limit + 1):
            #         reset_cells(board, cells)
                    
            #         if not cages:
            #             return False
                    
            #         # generate new number in prev cage to avoid being stuck
            #         while not edit_prev_cage(board, cages[len(cages) - limitEdit], (len(cages) - limitEdit), cage_sum):
            #             limitEdit += 1
            #             if (limitEdit > len(cages)):
            #                 limitEdit = 0
            #                 return False
                        
            #     num = random.randint(1, 4)
    

# def edit_prev_cage(board, cages, cage_idx, cage_sum):
#     cage_num, prev_cells = cages

#     for cell in prev_cells:
#         row, col = cell
#         temp = board[row][col]
#         board[row][col] = next cell
#         last board[row][col] = temp



#     reset_cells(board, prev_cells)

#     limit = 0
#     limitFlag = 0
#     numbers = [1, 2, 3, 4]

#     perms = permutations(numbers, len(prev_cells))
#     for perm in perms:
#         limit += 1

#     while not is_valid_cage(board, prev_cells):

#         print(f"\n[edit_prev_cage] tries: [{limitFlag}]")
#         print_boxes_layout(board)
#         print("\n")

#         # check if stuck
#         limitFlag += 1
#         if (limitFlag > limit + 1):
#             return False
            
#         # generate number on the cage
#         for cell in prev_cells:
#             row, col = cell
#             num = random.randint(1, 4)
#             while not is_to_sum(board, prev_cells, cage_sum):
#                 num = random.randint(1, 4)
#             board[row][col] = num

#     print(f"\n[edit_prev_cage] cage_idx: [{cage_idx}] final")
#     print_boxes_layout(board)
#     print("\n")

#     return True