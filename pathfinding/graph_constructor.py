import copy

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # self.graph = [[0 for _ in range(vertices)] for __ in range(vertices)]
        self.graph = {v: {} for v in range(vertices) }

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def neighbors(self, v):
        return self.graph[v].keys()

    @classmethod # makes first param is an instance of the class
    def from_existing(cls, edges):
        vertices = len(edges.keys())
        new_graph = cls(vertices) # = new Graph()
        new_graph.graph = copy.deepcopy(edges)

        return new_graph