#1463. Cherry Pickup II

#You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.
#You have two robots that can collect cherries for you:
#Robot #1 is located at the top-left corner (0, 0), and
#Robot #2 is located at the top-right corner (0, cols - 1).
#Return the maximum number of cherries collection using both robots by following the rules below:

#From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
#When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
#When both robots stay in the same cell, only one takes the cherries.
#Both robots cannot move outside of the grid at any moment.
#Both robots should reach the bottom row in grid.

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @cache
        def f(i, j, k):
            if i != m and 0 <= j < n and 0 <= k < n:
                res = 0
                for p in (-1, 0, 1):
                    for q in (-1, 0, 1):
                        res = max(res, f(i+1, j+p, k+q))
                res += grid[i][j] + grid[i][k]*(j != k)
                return res
            return 0

        return f(0, 0, n-1)
