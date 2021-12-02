class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}

    def add_vertex(self,label):
        if type(label) is not str:
            raise ValueError("Label must be a string")
        for key in self.graph_dict:
            if label == key:
               raise ValueError("Label already exists")
        self.graph_dict[label] = []
        return self.graph_dict

    def add_edge(self, src, dest, weight):
        pass
    # def print_edges(self):
    #     print(self.edges)


def main():
    my_graph = Graph(5)
    print(my_graph.add_vertex("A"))
    print(my_graph.add_vertex("B"))
    print(my_graph.add_vertex("C"))
    print(my_graph.add_vertex("B"))

if __name__ == "__main__":
    main()