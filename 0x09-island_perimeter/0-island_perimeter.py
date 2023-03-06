from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                return dfs(grid, r, c)


def dfs(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
        return 1  # boundary or water cell encountered
    if grid[r][c] == -1:
        return 0  # already visited cell
    grid[r][c] = -1  # mark the cell as visited
    perimeter = dfs(grid, r-1, c) + dfs(grid, r+1, c) + dfs(grid, r, c-1)\
        + dfs(grid, r, c+1)
    return perimeter
