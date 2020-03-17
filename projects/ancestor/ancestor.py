class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("vertex does not exist...")

# ancestors
# 1 3   2 3   3 6   5 6   5 7   4 5   4 8   8 9   11 8   10 1


def earliest_ancestor(ancestors, starting_node):
    # make a graph
    graph = Graph()

    for pair in ancestors:
        # parent is the first pair
        parent = pair[0]
        graph.add_vertex(pair[0])
        # child is the second pair
        child = pair[1]
        graph.add_vertex(pair[1])
        # add a directed edge
        graph.add_edge(parent, child)
