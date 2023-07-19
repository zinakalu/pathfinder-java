from pathfinding.graph_constructor import Graph

class BellmanGraph(Graph):

    def bellman_ford(self, src):
        
        distance = [float('inf')]* self.V
        distance[src] = 0

        for _ in range(self.V -1):
            for u in range(self.V):
                for v, weight in self.graph[u].items():
                    if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                        distance[v] = distance[u] + weight

        for u in range(self.V):
            for v, weight in self.graph[u].items():
                if distance[u] != float('inf') and distance[u] + weight < distance[v]:
                    print("Graph contains negative weight cycle")
                    return

        return distance



        # for _ in range(self.V -1):
        #     for edge in self.graph:     
        #         if distance[edge.u] != float('inf') and distance[edge.u] + edge.weight < distance[edge.v]:
        #             distance[edge.v] = distance[edge.u] + edge.weight

        # for edge in self.graph:     
        #     if distance[edge.u] != float('inf') and distance[edge.u] + edge.weight < distance[edge.v]:
        #         print("Graph contains negative weight cycle")
        #         return

        # return distance