class Solution:
    def videoStitching(self, clips, T):
        clips.sort()
        dp = [0] * 101
        for clip in clips:
            if clip[0] == 0:
                dp[clip[1]] = 1
                continue
            minnum = float('inf')
            for t in range(clip[0], clip[1]):
                if dp[t] != 0:
                    minnum = min(minnum, dp[t]+1)
            if minnum != float('inf'):
                if dp[clip[1]] == 0:
                    dp[clip[1]] = minnum
                else:
                    dp[clip[1]] == min(minnum, dp[clip[1]])
        minnum = float('inf')
        for i in range(T, 101):
            if dp[i] != 0:
                minnum = min(minnum, dp[i])
        return minnum if minnum != float('inf') else -1
        
        # dp = [[(0, 0, 1)] * len(clips) for _ in range(len(clips))]
        # for i, c in enumerate(clips):
        #     dp[i][i] = (c[0], c[1], 1)
        # for i in range(len(clips)):
        #     for j in range(i+1, len(clips)):
        #         dp[i][j] = ()


    # MINNUM = float('inf')

    # def videoStitching(self, clips, T: int) -> int:
    #     def buildtree():
    #         root = []
    #         i = 0
    #         graph = dict()
    #         while i < len(sortedclips):
    #             if sortedclips[i][0] == 0:
    #                 root.append(i)
    #             elif sortedclips[i][0] > T:
    #                 break
    #             graph[i] = []
    #             for j in range(i+1, len(sortedclips)):
    #                 if sortedclips[i][1] > sortedclips[j][1]:
    #                     continue
    #                 if sortedclips[i][1] >= sortedclips[j][0]:
    #                     graph[i].append(j)
    #                 else:
    #                     break
    #             i += 1
    #         return root, graph

    #     def dfs(start, graph, pathlen):
    #         if sortedclips[start][1] >= T:
    #             self.MINNUM = min(self.MINNUM, pathlen+1)
    #         elif start in graph:
    #             for neb in graph[start]:
    #                 dfs(neb, graph, pathlen+1)

    #     sortedclips = sorted(clips)
    #     if sortedclips[0][0] != 0 or sortedclips[-1][1] < T:
    #         return -1

    #     root, graph = buildtree()
    #     for start in root:
    #         dfs(start, graph, 0)
    #     return self.MINNUM if self.MINNUM != float('inf') else -1

if __name__ == "__main__":
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    T = 10
    sol = Solution()
    print(sol.videoStitching(clips, T))
