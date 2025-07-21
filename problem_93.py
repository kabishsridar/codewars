"""
Hello. I hope you know something about Graph Theory. In this simple task lets implement our own class for future use. Don't be scared of long description!

The class Graph represents an undirected graph of vertices named 0 through V - 1. It supports 2 primary operations:

add an edge to the graph
iterate over all of the vertices adjacent to a vertex.
And provides a way for returning the number of vertices V and the number of edges E. Parallel edges and self-loops are permitted. Self-loop v-v appears in the adjacency list of v twice.

Let's see an example:

Construct a graph with 3 vertices and add some edges

g = Graph(3)
g.add_edge(0, 1)
g.add_edge(2, 2)
After this you should get:

g.V returns  3
g.E returns  2
g.adj returns [ [1], [0], [2, 2] ]
g.adj[2] returns [2,2] and so on..    
So. basically we have something like this:


Be aware that the self.adj field should keep track of the order in which the vertices were added. Meaning that, for example:

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 3)
g.add_edge(0, 2)

should lead to:
g.adj == [[1,3,2], [0], [0], [0]]

You should raise your own IllegalArgumentError on negative number of vertices in ctor or if add_edge gets incorrect args.
"""
class IllegalArgumentError(ValueError):
    pass


class Graph:
    def __init__(self, V):
        if V < 0:
            raise IllegalArgumentError("Number of vertices must be non-negative")
        self.V = V
        self.E = 0
        self.adj = []
        i = 0
        while i < V:
            self.adj.append([])
            i += 1

    def add_edge(self, v, w):
        if v < 0 or v >= self.V or w < 0 or w >= self.V:
            raise IllegalArgumentError(f"Vertices {v} and {w} must be between 0 and {self.V - 1}")
        self.adj[v].append(w)
        self.adj[w].append(v)
        self.E += 1
