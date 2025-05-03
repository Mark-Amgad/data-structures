class Graph:
    def __init__(self,is_directed = False):
        self.graph = {}
        self.is_directed = is_directed


    def add_vertex(self, vertex:int):
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, vertex1:int, vertex2:int, weight:int):
        if vertex1 not in self.graph:
            self.graph[vertex1] = {}

        if vertex2 not in self.graph:
            self.graph[vertex2] = {}

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