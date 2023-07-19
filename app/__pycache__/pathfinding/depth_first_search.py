from .graph_constructor import Graph #or pathfinding.graph_constructor


class DFSGraph(Graph):

    def dfs(self,start):
        results = []
        visited = set()


        def traverse(current_node):
            results.append(current_node)
            visited.add(current_node)

            neighbors = self.neighbors(current_node)

            for neighbor in neighbors:
                if not neighbor in visited:
                    traverse(neighbor)
            

        traverse(start) 
        return results