"""
second trial

recursive version

time complexity O(|V| +|E|)
"""


class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def recursiveHelper(start):
            ret = []
            if start == len(graph)-1:
                return [[start]]
            for node in graph[start]:
                nextpath = recursiveHelper(node)
                if nextpath:
                    for path in nextpath:
                        ret.append([start] + path)
            return ret

        return recursiveHelper(0)

if __name__ == "__main__":
    graph = [[1, 2], [3], [3], []]
    sol = Solution()
    print(sol.allPathsSourceTarget(graph))