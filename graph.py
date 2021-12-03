class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        self.num_vertices = 0

    def add_vertex(self, label):
        if type(label) is not str:
            raise ValueError("Label must be a string")
        for key in self.graph_dict:
            if label == key:
               raise ValueError("Label already exists")
        self.graph_dict[label] = []
        self.num_vertices += 1
        return self.graph_dict

    def get_vertex(self, label):
        if type(label) is not str:
            raise ValueError("Label must be a string")
        for key in self.graph_dict:
            if label == key:
               return key, self.graph_dict[key]
    
    def add_edge(self, src, dest, weight):
        if src not in self.graph_dict:
            edge_val = self.add_vertex(src)
        if dest not in self.graph_dict:
            edge_val = self.add_vertex(dest)
        self.graph_dict

# class Vertex:
#     def __init__(self, key):
#         self.id = key
#         self.connected_to = {}

#     def add_neighbor(self, neighbor, weight=0):
#         self.connected_to[neighbor] = weight

#     def __str__(self):
#         return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connected_to])
#     def get_connections(self):
#         return self.connected_to.keys()
#     def get_id(self):
#         return self.id
#     def get_weight(self, neighbor):
#         return self.connected_to[neighbor]

def main():
    my_graph = Graph(5)
    print(my_graph.add_vertex("A"))
    print(my_graph.add_vertex("B"))
    print(my_graph.add_vertex("C"))
    # print(my_graph.num_vertices)
    print(my_graph.get_vertex("C"))
    # print(my_graph.add_vertex("B"))

if __name__ == "__main__":
    main()
    