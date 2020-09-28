from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def breadth_first_search(self, starting_vertex):
        queue = [starting_vertex]
        visited_vertex = [starting_vertex]
        while queue:
            deque_item = queue.pop(0)
            print(deque_item, end=" ")
            for item in self.graph[deque_item]:
                if item not in visited_vertex:
                    queue.append(item)
                    visited_vertex.append(item)


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print ("Following is Breadth First Traversal (starting from vertex 2)")
g.breadth_first_search(2)