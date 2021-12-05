class Graph:
    def __init__(self):
        # self.edges = edges
        self.graph_dict = {}
        self.num_vertices = 0
        # self.edge_list = []

    def add_vertex(self, label):
        if type(label) is not str:
            raise ValueError("Label must be a string")
        for key in self.graph_dict:
            if label == key:
                raise ValueError("Label already exists")
        self.num_vertices += 1
        new_vertex = Vertex(label)
        self.graph_dict[label] = new_vertex
        return self.graph_dict

    def get_vertex(self, label):
        if type(label) is not str:
            raise ValueError("Label must be a string")
        for key in self.graph_dict:
            if label == key:
                return key, self.graph_dict[key]
            else:
                raise ValueError("Key not found")
    def add_edge(self, src, dest, weight):
        if src not in self.graph_dict:
            edge_val = self.add_vertex(src)
        if dest not in self.graph_dict:
            edge_val = self.add_vertex(dest)
        if src in self.graph_dict and dest in self.graph_dict:
            self.graph_dict[src].add_neighbor(dest, weight)
            self.graph_dict[dest].add_neighbor(src, weight)
            return self.graph_dict[src].connected_to
        else:
            return False

    def __str__(self):
        for key in self.graph_dict:
            yield self.graph_dict[key]
    def __iter__(self):
        return iter(self.graph_dict.values())

class Vertex:
    def __init__(self, label):
        self.id = label
        self.connected_to = []

    # def add_neighbor(self, neighbor, weight=0):
    #     self.connected_to[neighbor] = weight
    def add_neighbor(self, v, weight):
        if v not in self.connected_to:
            self.connected_to.append((v, weight))
            self.connected_to.sort()

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])

    def get_connections(self):
        for i in self.connected_to:
            print(type(self.connected_to[i]))
            return self.connected_to[i]
        # return self.connected_to.keys(), self.connected_to.values()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.connected_to[neighbor]


def main():
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    print(my_graph.add_edge("A", "B", 2.0))
    print(my_graph.add_edge("A", "C", 5.0))
    print(my_graph.graph_dict)
    # print(my_graph.get_vertex("A"))
    # my_graph.add_edge("A", "B", 2.0)
    # my_graph.add_edge("A", "C", 5.0)
    # print(my_graph.num_vertices)
    # print(my_graph.get_vertex("C"))
    # print(my_graph.add_vertex("B"))


if __name__ == "__main__":
    main()
