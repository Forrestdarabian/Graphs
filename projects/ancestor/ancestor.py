class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


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
    # make a queue
    queue = Queue()

    for pair in ancestors:
        # parent is the first pair
        parent = pair[0]
        graph.add_vertex(parent)
        # child is the second pair
        child = pair[1]
        graph.add_vertex(child)
        # add a directed edge
        graph.add_edge(child, parent)

    # enqueue the starting node since we want the longest path
    queue.enqueue([starting_node])

    longest_path_length = 0

    # while the queue isnt empty, dequeue the next path
    while queue.size() > 0:
        path = queue.dequeue()
        # current person is the last thing in the path
        current_node = path[-1]

        if len(path) > longest_path_length:
            longest_path_length = len(path)

        # using bfs, set neighbors equal to the current node set
        neighbors = graph.vertices[current_node]
        # create our for loop
        for ancestor in neighbors:
            # copy the path
            path_copy = list(path)
            # append the ancestor
            path_copy.append(ancestor)
            # enqueue the copied path
            queue.enqueue(path_copy)
