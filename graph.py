"""Graph ADT Module"""
import math
class Graph:
    """Graph class"""
    def __init__(self):
        """init method"""
        self.graph_dict = {}
        self.num_vertices = 0

    def add_vertex(self, label):
        """add vertex to the graph"""
        if type(label) is not str:
            raise ValueError("Label must be a string")
        for key in self.graph_dict:
            if label == key:
                raise ValueError("Label already exists")
        self.num_vertices += 1
        new_vertex = Vertex(label)
        self.graph_dict[label] = new_vertex
        return self
    def get_vertex(self, label):
        """find vertex and return if found"""
        if type(label) is not str:
            raise ValueError("Label must be a string")
        for key in self.graph_dict:
            if label == key:
                return key, self.graph_dict[key]
        raise ValueError("Key not found")
    def add_edge(self, src, dest, weight):
        """add edge between vertices"""
        if len(src) > 1 or len(dest) > 1:
            raise ValueError("Not a valid graph node")
        if type(weight) is not float:
            raise ValueError("Not a valid weight")
        if src not in self.graph_dict:
            edge_val = self.add_vertex(src)
        if dest not in self.graph_dict:
            edge_val = self.add_vertex(dest)
        if src in self.graph_dict and dest in self.graph_dict:
            self.graph_dict[src].add_neighbor(dest, weight)
            # self.graph_dict[dest].add_neighbor(src, weight)
            return self #.graph_dict[src].connected_to  
        return False
    def get_weight(self, src, dest):
        """get weight of vertices"""
        edge_list = self.get_vertex(src)[1].connected_to
        for i in edge_list:
            if i[0] == dest:
                return i[1]
        return math.inf

    def bfs(self, starting_vertex):
        """Breadth first search"""
        queue = []
        starting_vertex.distance = 0
        for vertex in starting_vertex.connected_to:
            self.graph_dict[vertex].distance = starting_vertex.distance + 1
            queue.append(vertex)
        while len(queue) > 0:
            pop_queue = queue.pop(0)
            node_v = self.graph_dict[pop_queue]

            for vertex in node_v.connected_to:
                pass
    def __iter__(self):
        """iter method"""
        return iter(self.graph_dict.values())

class Vertex:
    """Vertext class"""
    def __init__(self, label):
        """init method"""
        self.id = label
        self.connected_to = []
    def add_neighbor(self, vertex, weight):
        """add_neighbor"""
        if vertex not in self.connected_to:
            self.connected_to.append((vertex, weight))
            self.connected_to.sort()
    def __str__(self):
        """str function"""
        # return str(self.id) + ' connectedTo: ' + str([x for x in self.connected_to])
        return str(self.id) + ' connectedTo: ' + str(self.connected_to)
    def get_connections(self):
        """get_connections or edges"""
        for i in self.connected_to:
            print(type(self.connected_to[i]))
            return self.connected_to[i]

    def get_id(self):
        """get id of a vertex"""
        return self.id



def main():
    """Main function"""
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    print(my_graph.add_edge("A", "B", 2.0))
    print(my_graph.add_edge("A", "C", 5.0))
    for key in my_graph.graph_dict:
        print(f"{my_graph.graph_dict[key]}")
if __name__ == "__main__":
    main()
