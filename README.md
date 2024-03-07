# [Killer-Sodoku-using-Local-Search](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search)

<p>
  Killer 4x4 Sudoku is a variant of the classic Sudoku puzzle, but with a twist. 
  In addition to the usual rules of Sudoku (wherein each row, column, and 2x2 subgrid must contain the numbers 1 through 4 without repetition), Killer Sudoku introduces cages.
</p>

------------------

## RULES

<p>
  In Killer Sudoku, the grid is divided into cages, each containing a set of cells. The objective is to fill in the grid with numbers such that:
</p>

1. Each row contains the numbers 1 through 4 without repetition.
2. Each column contains the numbers 1 through 4 without repetition.
3. Each 2x2 subgrid contains the numbers 1 through 4 without repetition.
4. The numbers within each cage sum up to a specified value.

_The goal of the puzzle is to fill in the entire grid while satisfying all these conditions._

------------------

## ALGORITHM

<p>
  The Killer Sudoku solver utilizes a hill-climbing algorithm to iteratively improve the current solution until a satisfactory solution is found. 
  The hill-climbing algorithm is a local search algorithm that explores neighboring solutions and moves towards better solutions based on an evaluation function.
</p>

### Steps of the Hill-Climbing Algorithm:

1. **Initialization**: Start with an initial solution, which can be generated randomly or by some heuristic method.
2. **Evaluation**: Calculate the "quality" of the current solution using an evaluation function. In the context of Killer Sudoku, the evaluation function could be based on the number of conflicts or errors in the solution.
3. **Neighborhood Generation**: Generate neighboring solutions by applying local search operators. In the case of Killer Sudoku, these operators might involve swapping numbers within a cage or trying different number assignments.
4. **Neighbor Evaluation**: Evaluate each neighboring solution to determine if it improves upon the current solution. This evaluation can be based on criteria such as reducing the number of conflicts or increasing the number of correctly placed numbers.
5. **Move Selection**: Move to the best neighboring solution if it improves upon the current solution. Otherwise, terminate the algorithm.
6. **Termination**: Terminate the algorithm when a satisfactory solution is found or when a termination condition is met, such as reaching a maximum number of iterations or being unable to find a better solution.

### Advantages of Hill-Climbing Algorithm:

- Simple to implement and understand.
- Iteratively improves the solution without requiring a global view of the search space.
- Can be applied to a wide range of optimization problems.

### Limitations of Hill-Climbing Algorithm:

- Prone to getting stuck in local optima, especially in complex or high-dimensional search spaces.
- May not always find the globally optimal solution.
- Performance highly depends on the choice of initial solution and the evaluation function.

<p>
  This algorithm is used in the Killer Sudoku solver to efficiently search for solutions while satisfying the puzzle constraints.
</p>

------------------

## PROGRAM OUTPUT

<p>
  Below is an example of the output generated by the Killer Sudoku solver program. 
  This output showcases the process of inputting cages, assigning sums to cages, and ultimately solving the Killer Sudoku puzzle grid.
</p>

------------------

### User Input: _2x2 subgrid_
- Upper Left
  - Coord: `0,2 0,3 1,2 1,3`
  - Sum: `10`
- Upper Right
  - Coord: `0,2 0,3 1,2 1,3`
  - Sum: `10`
- Lower Left
  - Coord: `2,0 2,1 3,0 3,1`
  - Sum: `10`
- Lower Right
  - Coord: `2,2 2,3 3,2 3,3`
  - Sum: `10`

### OUTPUT
```
Welcome to 4x4 Killer Sudoku!
Please enter the cages:
 [0] [1] [2] [3]
+---+---+---+---+
|   |   |   |   | [0]
+---+---+---+---+
|   |   |   |   | [1]
+---+---+---+---+
|   |   |   |   | [2]
+---+---+---+---+
|   |   |   |   | [3]
+---+---+---+---+

Cage 1:
Available coordinates: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 0,0 0,1 1,0 1,1
Available cage sum is from [4] to [16]
Enter the sum for this cage: 10


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 2 |   |   | [0]
+---+---+---+---+
| 3 | 4 |   |   | [1]
+---+---+---+---+
|   |   |   |   | [2]
+---+---+---+---+
|   |   |   |   | [3]
+---+---+---+---+

Cage 2:
Available coordinates: [(0, 2), (0, 3), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 0,2 0,3 1,2 1,3
Available cage sum is from [4] to [16]
Enter the sum for this cage: 10


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 2 | 1 | 2 | [0]
+---+---+---+---+
| 3 | 4 | 3 | 4 | [1]
+---+---+---+---+
|   |   |   |   | [2]
+---+---+---+---+
|   |   |   |   | [3]
+---+---+---+---+

Cage 3:
Available coordinates: [(2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 2,0 2,1 3,0 3,1
Available cage sum is from [4] to [16]
Enter the sum for this cage: 10


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 2 | 1 | 2 | [0]
+---+---+---+---+
| 3 | 4 | 3 | 4 | [1]
+---+---+---+---+
| 1 | 2 |   |   | [2]
+---+---+---+---+
| 3 | 4 |   |   | [3]
+---+---+---+---+

Cage 4:
Available coordinates: [(2, 2), (2, 3), (3, 2), (3, 3)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 2,2 2,3 3,2 3,3
Available cage sum is from [4] to [16]
Enter the sum for this cage: 10


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 2 | 1 | 2 | [0]
+---+---+---+---+
| 3 | 4 | 3 | 4 | [1]
+---+---+---+---+
| 1 | 2 | 1 | 2 | [2]
+---+---+---+---+
| 3 | 4 | 3 | 4 | [3]
+---+---+---+---+

>>>Solution found:
 [0] [1] [2] [3]
+---+---+---+---+
| 2 | 1 | 4 | 3 | [0]
+---+---+---+---+
| 4 | 3 | 2 | 1 | [1]
+---+---+---+---+
| 3 | 4 | 1 | 2 | [2]
+---+---+---+---+
| 1 | 2 | 3 | 4 | [3]
+---+---+---+---+
```

------------------

### User Input: _Corner Center_
- Upper Left Corner
  - Coord: `0,0 0,1 1,0`
  - Sum: `8`
- Upper Right Corner
  - Coord: `0,2 0,3 1,3`
  - Sum: `6`
- Lower Left Corner
  - Coord: `2,0 3,0 3,1`
  - Sum: `9`
- Lower Right Corner
  - Coord: `2,3 3,2 3,3`
  - Sum: `7`
- Center
  - Coord: `1,1 1,2 2,1 2,2`
  - Sum: `10`

### OUTPUT
```
Welcome to 4x4 Killer Sudoku!
Please enter the cages:
 [0] [1] [2] [3]
+---+---+---+---+
|   |   |   |   | [0]
+---+---+---+---+
|   |   |   |   | [1]
+---+---+---+---+
|   |   |   |   | [2]
+---+---+---+---+
|   |   |   |   | [3]
+---+---+---+---+

Cage 1:
Available coordinates: [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 0,0 0,1 1,0
Available cage sum is from [3] to [12]
Enter the sum for this cage: 8


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 3 |   |   | [0]
+---+---+---+---+
| 4 |   |   |   | [1]
+---+---+---+---+
|   |   |   |   | [2]
+---+---+---+---+
|   |   |   |   | [3]
+---+---+---+---+

Cage 2:
Available coordinates: [(0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 0,2 0,3 1,3
Available cage sum is from [3] to [12]
Enter the sum for this cage: 6


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 3 | 1 | 2 | [0]
+---+---+---+---+
| 4 |   |   | 3 | [1]
+---+---+---+---+
|   |   |   |   | [2]
+---+---+---+---+
|   |   |   |   | [3]
+---+---+---+---+

Cage 3:
Available coordinates: [(1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0), (3, 1), (3, 2), (3, 3)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 2,0 3,0 3,1
Available cage sum is from [3] to [12]
Enter the sum for this cage: 9


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 3 | 1 | 2 | [0]
+---+---+---+---+
| 4 |   |   | 3 | [1]
+---+---+---+---+
| 2 |   |   |   | [2]
+---+---+---+---+
| 3 | 4 |   |   | [3]
+---+---+---+---+

Cage 4:
Available coordinates: [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 2), (3, 3)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 2,3 3,2 3,3
Available cage sum is from [3] to [12]
Enter the sum for this cage: 7


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 3 | 1 | 2 | [0]
+---+---+---+---+
| 4 |   |   | 3 | [1]
+---+---+---+---+
| 2 |   |   | 1 | [2]
+---+---+---+---+
| 3 | 4 | 2 | 4 | [3]
+---+---+---+---+

Cage 5:
Available coordinates: [(1, 1), (1, 2), (2, 1), (2, 2)]
Enter cage cells (row,col) separated by space (e.g., 1,1 1,2 2,1 2,2): 1,1 1,2 2,1 2,2
Available cage sum is from [4] to [16]
Enter the sum for this cage: 10


Updated board:
 [0] [1] [2] [3]
+---+---+---+---+
| 1 | 3 | 1 | 2 | [0]
+---+---+---+---+
| 4 | 1 | 2 | 3 | [1]
+---+---+---+---+
| 2 | 3 | 4 | 1 | [2]
+---+---+---+---+
| 3 | 4 | 2 | 4 | [3]
+---+---+---+---+

>>>Solution found:
 [0] [1] [2] [3]
+---+---+---+---+
| 4 | 3 | 1 | 2 | [0]
+---+---+---+---+
| 1 | 2 | 4 | 3 | [1]
+---+---+---+---+
| 2 | 1 | 3 | 4 | [2]
+---+---+---+---+
| 3 | 4 | 2 | 1 | [3]
+---+---+---+---+
```

------------------
