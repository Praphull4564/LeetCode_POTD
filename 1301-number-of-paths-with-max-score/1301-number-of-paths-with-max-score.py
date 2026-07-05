class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        MOD = 10**9 + 7
        n = len(board)
        memo = {}

        def solve(i, j):
            # Out of bounds or blocked
            if i < 0 or j < 0 or board[i][j] == 'X':
                return (-float('inf'), 0)

            # Reached start
            if board[i][j] == 'E':
                return (0, 1)

            if (i, j) in memo:
                return memo[(i, j)]

            bestScore = -float('inf')
            ways = 0

            for ni, nj in [(i - 1, j), (i, j - 1), (i - 1, j - 1)]:
                score, cnt = solve(ni, nj)

                if cnt == 0:
                    continue

                if board[i][j] != 'S':
                    score += int(board[i][j])

                if score > bestScore:
                    bestScore = score
                    ways = cnt
                elif score == bestScore:
                    ways = (ways + cnt) % MOD

            memo[(i, j)] = (bestScore, ways)
            return memo[(i, j)]

        score, ways = solve(n - 1, n - 1)

        if ways == 0:
            return [0, 0]

        return [score, ways]

# class Solution:
#     def pathsWithMaxScore(self, board: List[str]) -> List[int]:
#         res=[0,0]

#         dp=[[0]*len(board) for i in range(len(board))]

#         def solve(board,i,j,s):
#             if board[i][j]=='E':
#                 if s>res[0]:
#                     res[0]=s
#                     res[1]=1
#                     return
#                 elif s==res[0]:
#                     res[1]+=1
#                     return
#                 else:
#                     return
#             if i-1>=0:
#                 if board[i-1][j]=='E':
#                     solve(board,i-1,j,s)
#                 elif board[i-1][j]!='X':
#                     solve(board,i-1,j,s+int(board[i-1][j]))
#             if j-1>=0:
#                 if board[i][j-1]=='E':
#                     solve(board,i,j-1,s)
#                 elif board[i][j-1]!='X':
#                     solve(board,i,j-1,s+int(board[i][j-1]))
#             if i-1>=0 and j-1>=0:
#                 if board[i-1][j-1]=='E':
#                     solve(board,i-1,j-1,s)
#                 elif board[i-1][j-1]!='X':
#                     solve(board,i-1,j-1,s+int(board[i-1][j-1]))


#         solve(board,len(board)-1,len(board)-1,0)
#         return res