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
        if vertex_id not in self.vertices:
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

    # create variables that keep track of longest path and earliest ancestor
    longest_path_length = 1
    earliest_ancestor = -1

    # while the queue isnt empty, dequeue the next path
    while queue.size() > 0:
        path = queue.dequeue()
        # current person is the last thing in the path
        current_node = path[-1]

        # if length of path is equal to longest_path_length...
        if len(path) >= longest_path_length:
            # and if our current node is less than the earliest ancestor...
            if current_node < earliest_ancestor:
                # we need to update the longest path length
                longest_path_length = len(path)
                # and update the earliest ancestor
                earliest_ancestor = current_node

        # however, if our path is longer than the longest_path_length...
        if len(path) > longest_path_length:
            # update longest_path_length to track it
            longest_path_length = len(path)
            # update earliest ancestor to track it
            earliest_ancestor = current_node

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

    # return last element of array with longest path
    return earliest_ancestor
