# Killer-Sodoku-using-Local-Search
<p>
Killer 4x4 Sudoku is a variant of the classic Sudoku puzzle, but with a twist. In addition to the usual rules of Sudoku (wherein each row, column, and 2x2 subgrid must contain the numbers 1 through 4 without repetition), Killer Sudoku introduces cages.
</p>

------------------

<p>
  In Killer Sudoku, the grid is divided into cages, each containing a set of cells. The objective is to fill in the grid with numbers such that:
</p>

1. Each row contains the numbers 1 through 4 without repetition.
2. Each column contains the numbers 1 through 4 without repetition.
3. Each 2x2 subgrid contains the numbers 1 through 4 without repetition.
4. The numbers within each cage sum up to a specified value.

<i> The goal of the puzzle is to fill in the entire grid while satisfying all these conditions. </i>

----------------

<b> ALGORITHM

<p>
  Local search algorithms, such as the first-choice algorithm, are optimization techniques used to solve combinatorial optimization problems like Sudoku. In the context of solving Killer 4x4 Sudoku, the first-choice algorithm involves iteratively making changes to the current solution and evaluating whether these changes improve the solution. If an improvement is found, the change is accepted and the process continues. Otherwise, the change is discarded and a different change is attempted.

The first-choice algorithm starts with an initial solution and iteratively makes small changes, evaluating each change to see if it leads to a better solution. The process continues until either an optimal solution is found or a predefined stopping criterion is met. This approach is often used for problems where finding the optimal solution is computationally expensive, as it can quickly explore the solution space and find reasonably good solutions. However, it may not always guarantee finding the best possible solution.
</p>
