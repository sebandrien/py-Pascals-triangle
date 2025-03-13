# PY Pascal's triangle

Defines a function pascal_triangle that generates Pascal's Triangle with a specified number of rows, n. 

The function starts with an empty list triangle to store each row of the triangle. For each row, it begins with [1] since every row in Pascal’s Triangle starts with [1]. 

If there are already rows in triangle, it calculates the middle numbers by summing adjacent elements from the last row and adding these to the new row. Finally, it appends another 1 at the end of the row and adds the row to triangle. Once all rows are generated, the function returns the full triangle list. The provided code sets n = 5 to generate the first 5 rows, calls pascal_triangle, and prints each row. The rows follow Pascal's Triangle structure, where each element is the sum of the two elements above it from the previous row.

Example:
```py
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```
