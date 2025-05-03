from graph.Graph import Graph
import heapq


class GraphShortestPath(Graph):
    def shortest_path(self, start, end):
        """
        Parameters:
        start: The starting node.
        end: The ending node.

        Returns:
        A tuple containing the total distance of the shortest path and a list of nodes representing that path.
        """
        dist = None
        path = None
        if start not in self.graph or end not in self.graph:
            raise KeyError("Both start and end vertices must exist in the graph.")

        heap = [(0, start, [start])]
        visited = set()

        while heap:
            current_dist, current_vertex, path = heapq.heappop(heap)

            if current_vertex == end:
                return current_dist, path

            if current_vertex in visited:
                continue

            visited.add(current_vertex)

            for neighbor, weight in self.graph[current_vertex].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (current_dist + weight, neighbor, path + [neighbor]))

        return dist, path