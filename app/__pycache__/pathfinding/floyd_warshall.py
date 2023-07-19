from pathfinding.graph_constructor import Graph

class FloydWarshallGraph(Graph):
    def floyd_warshall(self):
        dist = {}

        for u in self.graph:
            dist[u] = {v: float('inf') for v in self.graph}
            dist[u][u] = 0

        for u in self.graph:
            for v, weight in self.graph[u].items():
                dist[u][v] = weight

        
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        return dist