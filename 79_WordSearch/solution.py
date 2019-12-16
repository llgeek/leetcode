class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not any(board): return not word
        if not word: return True
        m, n = len(board), len(board[0])
        def dfs(i, j, wordidx, visited):
            if wordidx == len(word):
                return True
            if not (0 <= i < m and 0 <= j < n):
                return False
            if board[i][j] != word[wordidx]:
                return False
            for x, y in {(0, 1), (0, -1), (1, 0), (-1, 0)}:
                nebi, nebj = x + i, y + j
                if (nebi, nebj) not in visited:
                    visited.add((nebi, nebj))
                    if dfs(nebi, nebj, wordidx + 1, visited):
                        return True
                    visited.discard((nebi, nebj))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0, {(i, j)}):
                        return True
        return False


if __name__ == "__main__":
    sol = Solution()
    board = [["a"]]
    word = "a"
    print(sol.exist(board, word))