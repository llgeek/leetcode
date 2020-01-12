class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not any(prerequisites):
            return True
        graph = {i: set() for i in range(numCourses)}
        indegree = {i: 0 for i in range(numCourses)}
        for prep in prerequisites:
            if not prep: continue
            for i in range(1, len(prep)):
                graph[prep[i-1]] = graph[prep[i-1]] | {prep[i]}
                indegree[prep[i]] = indegree[prep[i]] + 1
        stack = []
        for k in indegree.keys():
            if indegree[k] == 0:
                stack.append(k)
        if not stack:
            return False
        cnt = 0
        while stack:
            s = stack.pop()
            cnt += 1
            for neb in graph[s]:
                indegree[neb] -= 1
                if indegree[neb] == 0:
                    stack.append(neb)
        return cnt == numCourses

