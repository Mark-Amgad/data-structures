from graph.GraphShortestPath import GraphShortestPath


def test_graph_shortest_path():
    shortest_path_graph = GraphShortestPath()
    shortest_path_graph.add_vertex(1)
    shortest_path_graph.add_vertex(2)
    shortest_path_graph.add_vertex(3)
    shortest_path_graph.add_vertex(4)
    shortest_path_graph.add_vertex(5)

    shortest_path_graph.add_edge(1,2,1)
    shortest_path_graph.add_edge(2, 3, 1)
    shortest_path_graph.add_edge(3, 4, 1)
    shortest_path_graph.add_edge(4, 5, 1)
    shortest_path_graph.add_edge(1, 5, 8)

    distance ,shortest_path = shortest_path_graph.shortest_path(1,5)
    assert distance == 4
    assert shortest_path == [1,2,3,4,5]

def test_graph_shortest_path_2():
    shortest_path_graph = GraphShortestPath()
    shortest_path_graph.add_vertex(1)
    shortest_path_graph.add_vertex(2)
    shortest_path_graph.add_vertex(3)
    shortest_path_graph.add_vertex(4)
    shortest_path_graph.add_vertex(5)

    shortest_path_graph.add_edge(1,2,1)
    shortest_path_graph.add_edge(2, 3, 1)
    shortest_path_graph.add_edge(3, 4, 1)
    shortest_path_graph.add_edge(4, 5, 1)
    shortest_path_graph.add_edge(1, 5, 3)

    distance ,shortest_path = shortest_path_graph.shortest_path(1,5)
    assert distance == 3
    assert shortest_path == [1,5]
