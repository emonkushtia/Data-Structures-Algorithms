"""
    https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python

    Depth-first search (DFS), is an algorithm for tree traversal on graph or tree data structures.
    It can be implemented easily using recursion and data structures like dictionaries and arrays.
    DFS just like pre order traversing in binary tree

    The Algorithm:
    1.  Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
    2.  Repeat until all the nodes are visited, or the node to be searched is found.

    Time Complexity:
    Since all the nodes and vertices are visited, the time complexity for DFS on a graph is O(V + E)O(V+E),
    where VV is the number of vertexes and EE is the number of edges. In case of DFS on a tree,
    the time complexity is O(V)O(V), where VV is the number of nodes.

"""


# Using a Python dictionary to act as an adjacency list

def dfs_recursive(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.append(node)
        for neighbour in graph[node]:
            dfs_recursive(visited, graph, neighbour)


def dfs(graph, node):
    visited = []  # List to keep track of visited nodes.
    stack = []  # Initialize a queue
    visited.append(node)
    stack.append(node)

    while stack:
        s = stack.pop()
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                stack.append(neighbour)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
dfs_recursive([], graph, 'A')
print('\n')
dfs(graph, 'A')
