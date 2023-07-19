from pathfinding.graph_constructor import Graph

class DijkstraGraph(Graph):
    def dijkstra(self, start):
        distances = {source: float('inf') for source in self.graph.keys()}
        distances[start] = 0

        # queue =[node for node in self.graph.keys()]
        queue = list(self.graph.keys())

        while queue:
            u = min(queue, key=lambda node: distances[node])
            # queue.pop(0)
            queue.remove(u)

            for v in self.neighbors(u):
                # if v not in queue:
                alt_path = distances[u] + self.graph[u][v]
                if alt_path < distances[v]:
                    distances[v] = alt_path

        return distances    
        

        