# from itertools import permutations

# # Define the numbers
# numbers = [1, 2, 3, 4]
# perms = permutations(numbers, 3)

# temp = []

# print("[permu] Sets of three numbers whose sum equals 8:")
# for perm in perms:
#     if sum(perm) == 8:
#         temp.append(perm)

# print(f"temp: {temp}")
# print(f"temp[0]: {temp[0]}")

# tempB = temp[0]
# print(f"tempB[0]: {tempB[0]}")
# print(f"tempB[1]: {tempB[1]}")
# print(f"tempB[2]: {tempB[2]}")

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
    
    print(f"duplicates: {duplicates}")

# Example usage
board = [
    [1, 3, 1, 2],
    [4, 1, 2, 3],
    [2, 3, 4, 1],
    [3, 4, 2, 4]
]

find_duplicate_coordinates(board)
