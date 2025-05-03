from graph.Graph import Graph

graph = Graph()


graph.add_vertex(1)
graph.add_vertex(2)
graph.add_edge(1,2,1)
graph.add_vertex(3)
graph.add_edge(2,3,1)
graph.add_edge(1,3,1)
graph.display()
graph.remove_edge(1,2)
graph.display()