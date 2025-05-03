from typing import List


class Graph:
    def __init__(self,is_directed = False):
        self.graph = {}
        self.is_directed = is_directed


    def add_vertex(self, vertex:int):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1:int, vertex2:int, weight:int):
        if vertex1 not in self.graph or vertex2 not in self.graph:
            raise KeyError("Both vertices must exist in the graph.")

        if vertex2 not in self.graph[vertex1]:
            self.graph[vertex1][vertex2] = weight

        if not self.is_directed and vertex1 not in self.graph[vertex1]:
            self.graph[vertex2][vertex1] = weight



    def remove_vertex(self, vertex:int):
        if vertex in self.graph:
            for other_vertex in list(self.graph.keys()):
                if vertex in self.graph[other_vertex]:
                    del self.graph[other_vertex][vertex]

            del self.graph[vertex]



    def remove_edge(self, vertex1:int, vertex2:int):
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            del self.graph[vertex1][vertex2]

        if not self.is_directed and vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            del self.graph[vertex2][vertex1]

    def display(self):
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                print(f"{vertex} ------{self.graph[vertex][edge]}-------> {edge} ")
        print("----------------------------------------------------")

    def get_adjacent_vertices(self, vertex):
        return list(self.graph.get(vertex, {}).keys())

    def tour_length(self, tour:List[int]):
        """
        Parameters:
        - tour: A list of vertices representing a tour. A tour ends and starts in the initial vertex. This is assumed, so you should not write the last vertice.
        """
        if tour and tour[0] == tour[-1] and len(tour) > 1:
            raise ValueError("Tour should not include the return to the starting vertex.")
        total_length = 0
        for i in range(len(tour)):
            weight = self._get_edge_weight(tour[i], tour[(i + 1) % len(tour)])
            if weight == float('inf'):  # Check for missing edge
                return float('inf')  # Tour is invalid if any edge is missing
            total_length += weight
        return total_length


    def get_vertex(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        return None

    def _get_edge_weight(self, src, dest):
        return self.graph[src].get(dest, float('inf'))