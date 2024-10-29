from typing import List, Tuple


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """
        Finds the maximum number of moves in a grid.

        Args:
          grid (List[List[int]]): The input grid of integers.

        Returns:
          int: The maximum number of moves.
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        dp = [[-1] * cols for _ in range(rows)]

        def helper(ri: int, cj: int) -> int:
            """
            Helper function to calculate the maximum number of moves from a given cell.

            Args:
              ri (int): The row index of the current cell.
              cj (int): The column index of the current cell.

            Returns:
              int: The maximum number of moves from the current cell.
            """
            if dp[ri][cj] != -1:
                return dp[ri][cj]

            directions: List[Tuple[int, int]] = [
                (ri - 1, cj + 1),
                (ri, cj + 1),
                (ri + 1, cj + 1),
            ]
            max_moves = 0

            for dr, dc in directions:
                if 0 <= dr < rows and 0 <= dc < cols and grid[dr][dc] > grid[ri][cj]:
                    max_moves = max(max_moves, helper(dr, dc) + 1)

            dp[ri][cj] = max_moves
            return dp[ri][cj]

        return max(helper(i, 0) for i in range(rows))
