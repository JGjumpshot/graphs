"""Graph ADT Module"""
import math
import heapq
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
            try:
                float(weight)
            except:
                raise ValueError("Not a valid weight")
        if src not in self.graph_dict:
            edge_val = self.add_vertex(src)
        if dest not in self.graph_dict:
            edge_val = self.add_vertex(dest)
        if src in self.graph_dict and dest in self.graph_dict:
            self.graph_dict[src].add_neighbor(dest, weight)
            return self
        return False
    def get_weight(self, src, dest):
        """get weight of vertices"""
        edge_list = self.get_vertex(src)[1].connected_to
        for i in edge_list:
            if i[0] == dest:
                return i[1]
        return math.inf

    def bfs(self, start_vertex):
        """Breadth first search"""
        start_node = self.get_vertex(start_vertex)
        queue, visited = [start_node[0]], []
        while queue:
            vertex = queue.pop(0)
            if vertex in visited:
                continue
            visited.append(vertex)
            new_vertex_var = self.get_vertex(vertex)
            for neighbor in new_vertex_var[1].connected_to:
                push_stack = self.get_vertex(neighbor[0])
                queue.append(push_stack[0])
                start_node = push_stack
        return iter(visited)
      
    def dfs(self, start_node):
        """Depth first search"""
        start_node = self.get_vertex(start_node)
        stack, visited = [start_node[0]], []
        while stack:
            vertex = stack.pop()
            if vertex in visited:
                continue
            visited.append(vertex)
            new_vertex_var = self.get_vertex(vertex)
            for neighbor in new_vertex_var[1].connected_to:
                push_stack = self.get_vertex(neighbor[0])
                stack.append(push_stack[0])
                start_node = push_stack
        return iter(visited)
    def dsp(self, src, dest):
        """DSP between 2 vertices"""
        distances = {vertex: math.inf for vertex in self.graph_dict}
        distances[src] = 0
        previous = {vertex: [] for vertex in self.graph_dict}
        pq = [(0, src)]
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue
            previous[src] = [src]
            for neighbor, weight in self.graph_dict[current_vertex].connected_to:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    previous[neighbor] = list(previous[current_vertex])
                    previous[neighbor].append(neighbor)
                    distances[neighbor] = distance 
                    heapq.heappush(pq, (distance, neighbor))

        return (distances[dest], previous[dest])
        
    def dsp_all(self, starting_vertex):
        """DSP for all vertices"""
        distances = {vertex: math.inf for vertex in self.graph_dict}
        distances[starting_vertex] = 0
        previous = {vertex: [] for vertex in self.graph_dict}
        pq = [(0, starting_vertex)]
        # for vertex in self.graph_dict:
        #     previous.append(None)
        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue
            previous[starting_vertex] = [starting_vertex]
            for neighbor, weight in self.graph_dict[current_vertex].connected_to:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    previous[neighbor] = list(previous[current_vertex])
                    previous[neighbor].append(neighbor)
                    distances[neighbor] = distance 
                    heapq.heappush(pq, (distance, neighbor))

        return previous
    def __str__(self):
        formatted_str = f"digraph G {{\n"
        for node in self.graph_dict:
            for neighbor in self.graph_dict[node].connected_to:
                formatted_str += f"   {self.graph_dict[node].id} -> {neighbor[0]} [label=\"{neighbor[1]}\",weight=\"{neighbor[1]}\"];\n"
        return formatted_str + "}\n"
    def __iter__(self):
        """iter method"""
        return iter(self.graph_dict.values())

class Vertex:
    """Vertex class"""
    def __init__(self, label):
        """init method"""
        self.id = label
        self.connected_to = []
        self.weight = 0
    def add_neighbor(self, vertex, weight):
        """add_neighbor"""
        if vertex not in self.connected_to:
            self.weight = weight
            self.connected_to.append((vertex, weight))
            self.connected_to.sort()
    def __str__(self):
        """str function"""
        return str(self.id) + ' connectedTo: ' + str(self.connected_to)
    def get_connections(self):
        """get_connections or edges"""
        for i in self.connected_to:
            return self.connected_to[i]
    def get_id(self):
        """get id of a vertex"""
        return self.id



def main():
    """Main function"""
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")

    g.add_edge("A", "B", 2.0)
    g.add_edge("A", "F", 9.0)
    
    g.add_edge("B", "C", 8.0)
    g.add_edge("B", "D", 15.0)
    g.add_edge("B", "F", 6.0)

    g.add_edge("C", "D", 1.0)
    
    g.add_edge("E", "C", 7.0)
    g.add_edge("E", "D", 3.0)
    
    g.add_edge("F", "B", 6.0)
    g.add_edge("F", "E", 3.0)
    print(g)
    print("starting DFS with vertex A")
    for i in g.dfs("A"):
        print(i, end=" ")
    print()
    print("starting BFS with vertex A")
    for j in g.bfs("A"):
        print(j, end=" ")
    print()
    print(g.dsp("A", "F"))
    print(g.dsp_all("A"))
if __name__ == "__main__":
    main()
