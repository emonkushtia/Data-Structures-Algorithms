"""
    https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python

    Breath-first search (BFS) is an algorithm used for tree traversal on graphs or tree data structures.
    BFS can be easily implemented using recursion and data structures like dictionaries and lists.
    BFS just like level order traversing in binary tree

    The Algorithm:
    1   Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
    2.  If there are no remaining adjacent vertices left, remove the first vertex from the queue.
    3.  Repeat step 1 and step 2 until the queue is empty or the desired node is found.

    Time Complexity:
    Since all of ​the nodes and vertices are visited, the time complexity for BFS on a graph is O(V + E)O(V+E);
    where VV is the number of vertices and EE is the number of edges.
"""

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def bfs(graph, node):
    visited = []  # List to keep track of visited nodes.
    queue = []  # Initialize a queue
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
bfs(graph, 'A')
