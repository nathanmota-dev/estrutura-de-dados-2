from collections import defaultdict, deque

class Graph:
    def __init__(self, qtd):
        self.qtd = qtd
        self.adj = defaultdict(list)

    def addEdge(self, graph, graph2):
        self.adj[graph].append(graph2)

    def DFSUtil(self, graph, visited):
        visited[graph] = True
        print(graph, end=' ')

        for next in self.adj[graph]:
            if not visited[next]:
                self.DFSUtil(next, visited)

    def DFS(self, graph):
        visited = [False] * self.qtd
        self.DFSUtil(graph, visited)

    def BFS(self, graph):
        visited = [False] * self.qtd
        queue = deque()

        visited[graph] = True
        queue.append(graph)

        while queue:
            graph = queue.popleft()
            print(graph, end=' ')

            for n in self.adj[graph]:
                if not visited[n]:
                    visited[n] = True
                    queue.append(n)

# Aplicação
graphs = Graph(4)

graphs.addEdge(0, 1)
graphs.addEdge(0, 2)
graphs.addEdge(1, 2)
graphs.addEdge(2, 0)
graphs.addEdge(2, 3)
graphs.addEdge(3, 3)

print("DFS:", end=' ')
graphs.DFS(2)
print()

print("BFS:", end=' ')
graphs.BFS(2)
