"""
DFS to find an Eulerian cycle in an undirected graph
"""
import copy
def findEulerianCycle(graph):
    graphcopy = copy.deepcopy(graph)
    if not graph:
        print('ERROR: graph is empty')
        return 
    
    totaledges = 0  #total number of edges in graph
    edgecnt = {}
    for vet, adjvets in enumerate(graph):
        if not adjvets:
            print('ERROR: vertex %d is disconnected' %vet)
            return
        if len(adjvets) & 1:
            print('ERROR: degree of vertex %d is odd' %vet)
            return
        totaledges += len(adjvets)
        edgecnt[vet] = len(adjvets)
    totaledges //= 2

    stack = [0]   # maintain a stack to keep vertices
    curvet = 0      # current vertex
    cycle = []      # final Eulerian cycle

    edgevisited = set()
    while stack:
        if edgecnt[curvet] != 0:
            stack.append(curvet)
            nextvet = graphcopy[curvet][-1]
            # pop out adjacent vertices whose edge has been visited
            while graphcopy[curvet] and (min(curvet, nextvet), max(curvet, nextvet)) in edgevisited:
                graphcopy[curvet].pop()
                nextvet = graphcopy[curvet][-1]
            graphcopy[curvet].pop()
            # mark all visted edge as visited
            edgevisited.add((min(curvet, nextvet), max(curvet, nextvet)))
            # pop out adjacent vertices whose edge has been visited
            # because in total one edge will be at most be added in edgevisted for once, so the time complexity for these two while is O(E)
            while graphcopy[nextvet] and (min(graphcopy[nextvet][-1], nextvet), max(graphcopy[nextvet][-1], nextvet)) in edgevisited:
                graphcopy[nextvet].pop()
            
            
            edgecnt[curvet] -= 1    
            edgecnt[nextvet] -= 1
            curvet = nextvet
            
        else:
            cycle.append(curvet)
            curvet = stack.pop()
    for i in range(len(graph)):
        if i not in set(cycle):
            print('ERROR: vertex %d is disconnected' %i)
            return
    if totaledges != len(cycle)-1:
        print('ERROR: No Euclerian cycle exists')
        return 
    return ''.join(map(str, cycle))

if __name__ == "__main__":
    # graph = [[1,2], [0,2], [0,1,3,4], [2,4], [2,3]]
    graph = [[1,2], [0, 2], [0,1]]
    print(findEulerianCycle(graph))


    


