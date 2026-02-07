"""
Problem Statement:

You are given a matrix as a list of lists (2D list of integers) and a list of command strings. Each command is one of the following formats:
- "swapRows i j": Swap the i-th and j-th rows (0-based indices).
- "swapColumns i j": Swap the i-th and j-th columns (0-based indices).
- "reverseRow i": Reverse the elements in the i-th row.
- "reverseColumn j": Reverse the elements in the j-th column.
- "rotate90Degrees": Rotate the entire matrix 90 degrees clockwise (transpose then reverse each row; shape may change if not square).

Apply the commands in the order given, modifying the matrix in place where possible, and return the final matrix after all operations.

Assumptions:
- The matrix is non-empty and rectangular (all rows have the same length).
- Commands are valid strings with correct formats and indices within bounds (no need for error checking in the code).
- For rotate90Degrees, the rotation is clockwise, and the function handles rectangular matrices by updating the shape.
- Operations are performed sequentially.

Example:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
commands = [
    "swapRows 0 2",       # -> [[7,8,9],[4,5,6],[1,2,3]]
    "swapColumns 1 2",    # -> [[7,9,8],[4,6,5],[1,3,2]]
    "reverseRow 1",       # -> [[7,9,8],[5,6,4],[1,3,2]]
    "reverseColumn 0",    # -> [[1,9,8],[5,6,4],[7,3,2]]
    "rotate90Degrees"     # -> [[7,5,1],[3,6,9],[2,4,8]]
]
Output: [[7, 5, 1], [3, 6, 9], [2, 4, 8]]
"""

def process_matrix(matrix, commands):
    if not matrix or not matrix[0]:
        return matrix  # Handle empty matrix
    
    for cmd in commands:
        parts = cmd.split()
        op = parts[0]
        
        if op == "swapRows":
            i = int(parts[1])
            j = int(parts[2])
            matrix[i], matrix[j] = matrix[j], matrix[i]
        
        elif op == "swapColumns":
            i = int(parts[1])
            j = int(parts[2])
            for outer in matrix:
                outer[i], outer[j] = outer[j], outer[i]
        
        elif op == "reverseRow":
            i = int(parts[1])
            matrix[i] = matrix[i][::-1]
        
        elif op == "reverseColumn":
            j = int(parts[1])
            # Extract, reverse, and reinsert column
            col = [outer[j] for outer in matrix]
            col.reverse()
            for r in range(len(matrix)):
                matrix[r][j] = col[r]
        
        elif op == "rotate90Degrees":
            # Rotate 90 degrees clockwise: transpose then reverse each row
            # Updates matrix in place (shape may change if not square)
            matrix[:] = [list(reversed(outer)) for outer in zip(*matrix)]
    
    return matrix

# Example usage (for testing):
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    commands = [
        "swapRows 0 2",
        "swapColumns 1 2",
        "reverseRow 1",
        "reverseColumn 0",
        "rotate90Degrees"
    ]
    result = process_matrix(matrix, commands)
    print(result)  # Output: [[7, 5, 1], [3, 6, 9], [2, 4, 8]]
