from pathfinding.graph_constructor import Graph


class AStarGraph(Graph):
    def a_star(self, start, goal):
        open_set = set([start])
        came_from = {}

        known_score = {vertex: float('inf') for vertex in self.graph.keys()}
        known_score[start] = 0

        heuristic_score = {vertex: float('inf') for vertex in self.graph.keys()}
        heuristic_score[start] = self.heuristic(start, goal)
       

        while open_set:
            print(open_set)
            current = min(open_set, key=lambda node: heuristic_score[node])
            print(current)
            open_set.remove(current)

            if current == goal: 
                return self.construct_path(came_from, current)

            for neighbor in self.neighbors(current):
                potential_path = known_score[current] + self.graph[current][neighbor]

                if potential_path < known_score[neighbor]:
                    came_from[neighbor] = current
                    known_score[neighbor] = potential_path
                    heuristic_score[neighbor] = potential_path + self.heuristic(neighbor, goal)

                    if neighbor not in open_set:
                        open_set.add(neighbor)
        return None 



    def construct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.insert(0, current)
        return path #all other algos should return a path for start and end

    def heuristic(self, node, goal):
        return 1