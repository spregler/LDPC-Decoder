
class Node:
    '''Node class'''
    def __init__(self, node_id):
        '''
        Args:
            node_id : int

        Attributes: 
            value : int
            neighbors : (list) of node_id values belonging to neighboring nodes.
        '''
        self.node_id = node_id
        self.value = 0
        self.neighbors = [] # Cannot be indexed by node_id. Use index()
    
    def add_neighbors(self, node_ids):
        '''
        Args:
            node_ids : (list) of node_id values belonging to neighboring nodes 

        Adds list of node_id values to neighbors list if not already in it.      
        '''
        for node_id in node_ids:
            if node_id not in self.neighbors:
                self.neighbors.append(node_id)

    def get_neighbors(self):
        '''Return: neighbors list'''
        return self.neighbors
    
    def set_value(self, value):
        '''Set node value'''
        self.value = value

    def get_value(self):
        '''Return: node value'''
        return self.value
    
    def get_id(self):
        '''Return: node_id'''
        return self.node_id


class VariableNode(Node):
    '''Variable Node class. Subclass of Node class'''
    def __init__(self, node_id):
        Node.__init__(self, node_id)


class CheckNode(Node):
    '''Check Node class. Subclass of Node class'''
    def __init__(self, node_id):
        Node.__init__(self, node_id)


class Edge:
    '''Edge class'''
    def __init__(self, node_id1, node_id2):
        '''
        Args:
            node_id1 : (int) node_id of variable node
            node_id2 : (int) node_id of check node
        
        Attributes: 
            value : int
            edge_id : (tuple) (node_id1, node_id2)
        '''
        self.node_id1 = node_id1
        self.node_id2 = node_id2
        self.edge_id = tuple([node_id1, node_id2])
        self.value = 0

    def set_value(self, value):
        '''Set value of edge'''
        self.value = value
    
    def get_value(self):
        '''Return: value of edge'''
        return self.value
    
    def get_id(self):
        '''Return: edge_id'''
        return self.edge_id


class BipartiteGraph:
    '''Bipartite Graph class'''
    def __init__(self, variable_nodes, check_nodes, edges):
        '''
        Args:
            variable_nodes : (list) of VariableNode objects
            check_nodes : (list) of CheckNode objects
            edges : (list) of edge primitives. An edge primitive is a tuple containing two neighboring nodes
        
        Attributes:
            edges : (dict) with {(node_id1, node_id2) : (Edge)}
        '''
        self.vnodes = variable_nodes # Can be indexed by node_id
        self.cnodes = check_nodes # Can be indexed by node_id
        self.edges = {}


        for edge in edges:
            self.add_edge(edge)
    
    def get_vnode(self, node_id):
        '''
        Arg:
            node_id : int
        
        Checks if a there is a Node object with the given node_id in variable_nodes. If not, it creates a Node object. 
        Returns Node object.
        '''

        # if not len(self.vnodes):
        #     newNode = VariableNode(node_id)
        #     self.vnodes.append(newNode)

        #     return newNode

        if node_id == self.vnodes[node_id].get_id():

            return self.vnodes[node_id]
        
        else:
            newNode = VariableNode(node_id)
            self.vnodes[node_id] = newNode

            return newNode
    
    def getVariableNodes(self):
        '''Return: list of VariableNode objects'''
        return self.vnodes

    def get_cnode(self, node_id):
        '''
        Checks if a node ID exists. If not, it creates a node with the given ID. Returns node object.
        '''
        # if not len(self.cnodes):
        #     newNode = CheckNode(node_id)
        #     self.cnodes.append(newNode)

        #     return newNode

        if node_id == self.cnodes[node_id].get_id():

            return self.cnodes[node_id]
        
        else:
            newNode = CheckNode(node_id)
            self.cnodes[node_id] = newNode

            return newNode
    
    def getCheckNodes(self):
        '''Return: list of CheckNode objects'''
        return self.cnodes
    
    def add_edge(self, edge_id):
        '''
        Arg:
            edge_id : (tuple) (node_id1, node_id2)

        Accepts an edge_id (an edge_id = is a tuple with of node_id values) and adds an Edge object to edges. Updates node
        objects' neighbors corresponding to node_id1 and node_id2.
        '''
        node1 = self.get_vnode(edge_id[0])
        node2 = self.get_cnode(edge_id[1])
        newEdge = Edge(edge_id[0],edge_id[1])

        self.edges[(node1.get_id(),node2.get_id())] = newEdge
        node1.add_neighbors([edge_id[1]])
        node2.add_neighbors([edge_id[0]])
    
    def readMessages(self, edge_ids):
        edge_vals = []
        for edge_id in edge_ids:
            edge_vals.append(self.edges[edge_id].get_value())

        return edge_vals
    
    # def sendMessage(self, edge_id):

def constructGraph(filename):
    N = None
    M = None
    max_col_weight = None
    max_row_weight = None
    col_weight_arr = []
    row_weight_arr = []
    vnodes = []
    cnodes = []
    edges = []

    Graph = BipartiteGraph(vnodes, cnodes, edges)
    
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file, start=1):
            if line_num == 1:
                N, M = map(int, line.split())
                vnodes = [VariableNode(i) for i in range(N)]
                cnodes = [CheckNode(j) for j in range(M)]
                line_num += 1
            
            elif line_num == 2:
                max_col_weight, max_row_weight = map(int, line.split())
                line_num += 1
            
            elif line_num == 3:
                col_weight_arr = [int(x) for x in line.split()]
                line_num += 1
            
            elif line_num == 4:
                row_weight_arr = [int(x) for x in line.split()]
                line_num += 1
            
            elif line_num < 5 + N:
                node_id = line_num-5
                print(line_num)
                line = [int(x) for x in line.split()]

                edges = [(node_id,j-1) for j in line]
                print(edges)
                
                for edge_id in edges:
                    Graph.add_edge(edge_id)

                line_num += 1
            
            else:
                break
        
        file.close()
        print("File closed!")
    
    return Graph


if __name__ == "__main__":
    a = [0,1,2,3,4,5,6,7,8,9]
    b = [0,1,2,3,4]

    vlist = [VariableNode(0), VariableNode(1), VariableNode(2), VariableNode(3), VariableNode(4), 
            VariableNode(5), VariableNode(6), VariableNode(7), VariableNode(8), VariableNode(9)]
    
    clist = [CheckNode(0), CheckNode(1), CheckNode(2), CheckNode(3), CheckNode(4)]

    elist = [
        [vlist[0].get_id(), clist[0].get_id()], 
        [vlist[0].get_id(), clist[1].get_id()], 
        [vlist[0].get_id(), clist[4].get_id()]]
    
    Graph = BipartiteGraph(vlist, clist, elist)
    vnodes = Graph.getVariableNodes()
    cnodes = Graph.getCheckNodes()
    edges = Graph.edges
    
    # # # edges[(0,0)].set_value(1)
    # # # edges[(0,1)].set_value(2)

    print(vnodes[0].get_neighbors())
    # # # print(cnodes[4].get_neighbors())
    print(Graph.readMessages(edges))

    # Graph = constructGraph(filename="alist.txt")