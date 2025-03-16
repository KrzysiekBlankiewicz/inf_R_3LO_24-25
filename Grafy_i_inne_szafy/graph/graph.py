import math

class Node:
    global_id = 0
    def __init__(self, x, y):
        self.id = Node.global_id
        Node.global_id += 1
        self.x = x
        self.y = y
        self.nghb = []

    def add_n(node):
        if node not in self.nghb:
            self.nghb.append(node)
            return True
        return False
    
    def remove_n(node):
        if node in self.nghb:
            self.nghb.remove(node)
            return True
        return False
    
    def distance(self, x, y):
        dx = self.x - x
        dy = self.y - y
        return math.sqrt(dx**2 + dy**2)


class GraphBuilder:
    def __init__(self, size):
        self.nodes = []
        self.max_x = size
        self.max_y = size
        self.node_radius = 10
        self.temp_node = None
        
    def add_node(self, node):
        self.nodes.append(node)

    def new_node(self, x, y):
        for n in self.nodes:
            if n.distance(x, y) < self.node_radius:
                return False
        new_n = Node(x, y)
        self.add_node(new_n)
        return new_n.id

    def new_vertex(self, n):
        if self.tempNode != None and \
                (self.tempNode != n) and \
                (self.tempNode not in n.nghb) and \
                (n.nghb not in self.tempNode.nghb):
            self.tempNode.nghb.append(n)
            n.nghb.append(self.tempNode)
            tempNode = None
            return True
        return False
    
    def get_node_at_pos(self, x, y):
        for n in self.nodes:
            if n.distance(x, y) < self.node_radius:
                return n
        return None
    
    def to_string(self):
        s = str(len(self.nodes)) + " " + \
            str(self.max_x) + " " + \
            str(self.max_y)
        
        for n in self.nodes:
            s += "\n" + str(n.id) + " " + \
                 str(n.x) + " " + \
                 str(n.y) + " "
            for nn in n.nghb:
                s += str(nn.id) + " "
        return s
    
    def print(self):
        f = open("yr.txt", 'w')
        f.writelines(self.to_string())
        f.close()



        
        
