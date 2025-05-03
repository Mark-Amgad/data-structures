from graph.Graph import Graph


def test_create_vertex():
    graph = Graph()
    graph.add_vertex(1)
    assert graph.get_vertex(1) is not None

def test_create_edge():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_edge(1, 2,1)
    assert 2 in graph.get_adjacent_vertices(1)
    assert 1 in graph.get_adjacent_vertices(2)

def test_remove_vertex():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_edge(1, 2,1)
    graph.add_edge(1, 2, 1)
    graph.remove_vertex(1)
    assert graph.get_vertex(1) is None
    assert 1 not in graph.get_adjacent_vertices(2)
    assert 1 not in graph.get_adjacent_vertices(3)


def test_remove_edge():
    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_edge(1, 2,1)
    graph.remove_edge(1,2)
    assert 1 not in graph.get_adjacent_vertices(2)
    assert 2 not in graph.get_adjacent_vertices(1)