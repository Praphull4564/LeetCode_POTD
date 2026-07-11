class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        dp = {}

        def solve(i, j):
            if i == len(w1):
                return len(w2) - j
            if j == len(w2):
                return len(w1) - i

            if (i, j) in dp:
                return dp[(i, j)]

            if w1[i] == w2[j]:
                dp[(i, j)] = solve(i + 1, j + 1)
            else:
                dp[(i, j)] = 1 + min(
                    solve(i + 1, j),     # Delete
                    solve(i, j + 1),     # Insert
                    solve(i + 1, j + 1)  # Replace
                )

            return dp[(i, j)]

        return solve(0, 0)