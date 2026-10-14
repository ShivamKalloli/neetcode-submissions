class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(r, c):
            if r >= row or c >= col or r < 0 or c < 0 or (r, c) in visited or grid[r][c] == "0":
                return

            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(row):
            for c in range(col):
                if grid[r][c] == "1" and (r, c) not in visited:
                    count += 1
                    dfs(r, c)
        return count