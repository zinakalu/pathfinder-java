from collections import deque
from pathfinding.graph_constructor import Graph

class BFSGraph(Graph):
     def breadth_first_search(self, start):
        visited = set([start])
        queue = deque([start])
        results=[start]


        while queue:
            current_node = queue.popleft()

            for neighbor in self.neighbors(current_node):
                if neighbor not in visited:
                    queue.append(neighbor)
                    results.append(neighbor)
                    visited.add(neighbor)
                
        return results