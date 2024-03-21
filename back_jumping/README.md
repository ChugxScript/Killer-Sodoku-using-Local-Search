# KILLER SUDOKU USING BACK JUMPING

## WHAT'S NEW?
  <p>
    The process of solving the sudoku change a lil bit. 
    Instead of generating numbers and solve the board after entering all the coordinates,
    it solves the board as you type the coordinates.
    Basically Back Jumping and Hill-climb Algorithm is applied to solve the board.
  </p>
  
## BOARD
  - Table

    ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/cb7cfa1b-c0b9-49a3-9ce8-ae94c0968d1b)
  - Coordinates

    ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/61da66b1-8a7d-4133-a5b0-0f1009c5f852)
    ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/44be5c14-b57b-402a-bab6-6d6600ae4e5c)
  - Let `(0|0) 0` be `(A|B) C`

    ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/1d5febc6-2e5a-4087-9b3c-d83f84548cdc)
    - **A** - represent the `Cage_group` or from the first cage you enter up to last cage
    - **B** - represent the `Cage_sum` or the total sum of number within the cage
    - **C** - represent the `Cell_num` or the number itself
  - 

## SAMPLE USAGE

**Random inputs**
1. Cage cells: `0,0 0,1`
  Cage sum: `5`
  ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/e9ce7620-dbd8-4570-bc0e-5e8a8afd4798)

2. Cage cells: `0,2 0,3`
  Cage sum: `5`
  ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/f8ff0625-2a74-4674-9886-53513f62efdd)

3. Cage cells: `1,0 2,0`
  Cage sum: `4`
  ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/f41e20f5-15a4-4900-9be7-02a427e67665)

4. Cage cells: `1,1 1,2 1,3`
  Cage sum: `7`
  ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/dd4f8de2-737a-42f0-8f4c-13b8e67f4e76)

5. Cage cells: `2,1 2,2`
  Cage sum: `7`
  
  ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/69835f83-82ff-4aaf-a2cf-f4e79dbd2ea8)

6. Cage cells: `2,3 3,3`
  Cage sum: `6`
  
  ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/9b19fa93-2383-4ced-a6d6-a8f5f43c5501)

7. Cage cells: `3,0 3,1 3,2`
  Cage sum: `6`
  ![image](https://github.com/ChugxScript/Killer-Sodoku-using-Local-Search/assets/101156843/e9cdfbb0-f8ae-4c99-8330-3863f4b15ffb)
