from collections import defaultdict


class Graph:

    def __init__(self):
        # if a key is accessed that is not in the dict, returns []
        self.graph = defaultdict(list)

    def addEdge(self, u, v, direction=1):
        # direction = 0 -> undirected
        # direction = 1 -> directed
        self.graph[u].append(v)
        if (direction == 0):
            self.graph[v].append(u)

    def printAdjList(self):
        for i in self.graph.keys():
            print(f"{i} -> {self.graph[i]}")

    def allNodes(self):
        set1 = set()
        for i in self.graph.keys():
            set1.add(i)
            for j in self.graph.get(i):
                set1.add(j)
        return list(set1)

    # BFS
    def bfs(self, src):
        visited = { i: False for i in self.allNodes() }
        visited[src] = True

        queue = []
        queue.append(src)

        while(queue):
            curr = queue.pop(0)
            print(curr, end=" ")
            for i in self.graph[curr]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    # DFS
    def dfs_part(self, v, visited):
        visited[v] = True
        print(v, end=' ')   
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_part(i, visited)
    
    def dfs(self, src):
        visited = { i: False for i in self.allNodes() }
        self.dfs_part(src, visited)



    # Topological Sort
    def tSort_part(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.tSort_part(i, visited, stack)
        stack.append(v)

    def tSort(self):
        visited = { i: False for i in self.allNodes() }
        stack = []
        for i in self.allNodes():
            if visited[i] == False:
                self.tSort_part(i, visited, stack)
        print(stack[::-1]) # return list in reverse order



    # Cycle Detection in Directed Graph BFS
    # def is_cyclic_ddb(self, vted, src):
    #     vted[src] = True
    #     queue = []
    #     queue.append(src)

    #     while(queue):
    #         front = queue.pop(0)
    #         for neighbour in self.graph[front]:
    #             if vted[neighbour] == True:      # Agar visited hai
    #                 return True
    #             else:
    #                 queue.append(neighbour)
    #                 vted[neighbour] = True

    #     return False

    def cycle_detection_directed_bfs(self):
        vted = { i: False for i in self.allNodes() }
        for i in self.allNodes():
            if vted[i] == False:
                if self.is_cyclic_ddb(vted, i):
                    return True
        return False


    # Cycle Detection in Undirected Graph BFS
    def is_cyclic_dub(self, vted, src):
        parent = dict()
        parent[src] = -1

        vted[src] = True
        queue = []
        queue.append(src)

        while(queue):
            front = queue.pop(0)
            for neighbour in self.graph[front]:
                if vted[neighbour] == True:      # Agar visited hai
                    if parent[front] != neighbour:  # and, jo parent of front hai neighbours me se vo hatao, uske siva koi already visited hai to cycle hai 
                        return True
                else:
                    queue.append(neighbour)
                    vted[neighbour] = True
                    parent[neighbour] = front

        return False

    def cycle_detection_undirected_bfs(self):
        vted = { i: False for i in self.allNodes() }
        for i in self.allNodes():
            if vted[i] == False:
                if self.id_cyclic_dub(vted, i):
                    return True
        return False



    # Cycle Detection in Directed Graph DFS
    def is_cyclic_ddd(self, src, vted, dfsvted):
        vted[src] = True
        dfsvted[src] = True

        for neighbour in self.graph[src]:
            if vted[neighbour] == False:
                if self.is_cyclic_ddd(neighbour, vted, dfsvted):
                    return True
            else:
                if dfsvted[neighbour] == True:
                    return True
        
        dfsvted[src] = False
        return False

    def cycle_detection_directed_dfs(self):
        vted = {i: False for i in self.allNodes()}  
        dfsvted = {i: False for i in self.allNodes()}        
        for i in self.allNodes():
            if vted[i] == False:
                if self.is_cyclic_ddd(i, vted, dfsvted):
                    return True
        return False


    # Cycle Detection in Undirected Graph DFS
    def is_cyclic_dud(self, src, vted, parent):
        vted[src] = True

        for neighbour in self.graph[src]:
            if vted[neighbour] == False:
                if self.is_cyclic_dud(neighbour, vted, src):
                    return True
            else:
                if parent != neighbour:
                    return True
                
        return False

    def cycle_detection_undirected_dfs(self):
        vted = { i: False for i in self.allNodes() }
        parent = -1
        for i in self.allNodes():
            if vted[i] == False:
                if self.is_cyclic_dud(i, vted, parent):
                    return True
        return False






    









g = Graph()

g.addEdge(1, 2, 0)
g.addEdge(1, 4, 0)

g.addEdge(2, 3, 0)
g.addEdge(2, 5, 0)
g.addEdge(2, 4, 0)


g.addEdge(3, 6, 0)

g.addEdge(4, 3, 0)
g.addEdge(4, 5, 0)

g.addEdge(5, 6, 0)


# a1 = g.allNodes()
# print(a1)

g.printAdjList()

g.tSort()



