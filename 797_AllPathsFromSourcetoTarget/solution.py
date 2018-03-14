class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        if not graph:
            return result
        if len(graph) == 1:
            return [0]
        stack = [(0, [])]
        while stack:
            curnode, curpath = stack.pop()
            if curnode == len(graph)-1:
                tmppath = curpath[:]
                tmppath.append(curnode)
                result.append(tmppath)
            for neb in graph[curnode]:
                tmppath = curpath[:]
                tmppath.append(curnode)
                stack.append((neb, tmppath))
        
        return result
