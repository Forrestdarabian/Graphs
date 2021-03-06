"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


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

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("vertex does not exist...")

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create a queue
        q = Queue()
        # Enqueue the starting vertex
        q.enqueue(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first vertex
            v = q.dequeue()
            # Check if its been visited
            if v not in visited:
                # If it hasnt...
                # Mark as visited
                print(v)
                visited.add(v)
                # Enqueue all its neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create a stack
        s = Stack()
        # Push the starting vertex
        s.push(starting_vertex)
        # Create a set to store visited vertices
        visited = set()
        # While the stack is not empty..
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
        # Check if its been visited
            if v not in visited:
                # If it hasnt...
                # Mark as visited
                print(v)
                visited.add(v)
        # Push all its neighbors
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # 3rd param added to where we visited
        # Base case
        if visited is None:
            # Visited becomes an empty set
            visited = set()

        # Add the starting vertex to visited
        visited.add(starting_vertex)
        print("Using Recursion", starting_vertex)
        # Recursively call itself for each edge, we dont have a queue
        for child_vertex in self.vertices[starting_vertex]:
            # Child vertex should not be in visited list
            if child_vertex not in visited:
                self.dft_recursive(child_vertex, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create a queue
        qq = Queue()
        # Enqueue A PATH TO the starting vertex
        qq.enqueue([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the queue is not empty...
        while qq.size() > 0:
            # Dequeue the first PATH
            path = qq.dequeue()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            vertex = path[-1]
            # Check if its been visited
            if vertex not in visited:
                # If it hasnt...
                # Mark as visited
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                # Enqueue A PATH TO all its neighbors
                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    # MAKE A COPY OF THE PATH
                    new_path.append(next_vertex)
                    # ENQUEUE THE COPY
                    qq.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create a STACK
        ss = Stack()
        # PUSH A PATH TO the starting vertex
        ss.push([starting_vertex])
        # Create a set to store visited vertices
        visited = set()
        # While the STACK is not empty...
        while ss.size() > 0:
            # POP the first PATH
            path = ss.pop()
            # GRAB THE VERTEX FROM THE END OF THE PATH
            vertex = path[-1]
            # Check if its been visited
            if vertex not in visited:
                # If it hasnt...
                # Mark as visited
                if vertex == destination_vertex:
                    return path
                visited.add(vertex)
                # PUSH A PATH TO all its neighbors
                for next_vertex in self.vertices[vertex]:
                    new_path = list(path)
                    # MAKE A COPY OF THE PATH
                    new_path.append(next_vertex)
                    # PUSH THE COPY
                    ss.push(new_path)

    def dfs_recursive(self, starting_vertex, targetValue, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # 3rd param added to where we visited
        # Base case
        if visited is None:
            # Visited becomes an empty set
            visited = set()
        if path is None:
            path = []

        # Add the starting vertex to visited
        visited.add(starting_vertex)
        print("Using Recursion", starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == targetValue:
            return path
        # Recursively call itself for each edge, we dont have a queue
        for child_vertex in self.vertices[starting_vertex]:
            # Child vertex should not be in visited list
            if child_vertex not in visited:
                new_path = self.dfs_recursive(
                    child_vertex, targetValue, visited, path)
                if new_path:
                    return new_path


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
