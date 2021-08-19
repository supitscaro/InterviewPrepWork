class Solution:
    def transpose(self, matrix):
        """
            [
                [1,2,3],
                [4,5,6],
                [7,8,9]
            ]

            [
                [1,4,7],
                [2,5,8],
                [3,6,9]
            ]

            [
                [1,2,3],
                [4,5,6]
            ]

            [
                [1, 4],
                [2, 5],
                [3, 6]
            ]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        new_matrix = [[0]*rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                new_matrix[col][row] = matrix[row][col]

        return new_matrix
