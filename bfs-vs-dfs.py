import sys
import time
from networkx.generators.random_graphs import erdos_renyi_graph

TGREEN =  '\033[32m'
TRED = '\033[31m'
TYELLOW = '\033[33m'
ENDC = '\033[m'

class BFSvsDFS:
    def __init__(self, inp=sys.argv[1:]):
        self.nodes = int(inp[0])
        self.probability = float(inp[1])
        self.start = int(inp[2])
        self.targ = int(inp[3])
        self.verbose = inp[4].upper()
        self.initgraph = erdos_renyi_graph(self.nodes, self.probability)
        self.alledges = list(self.initgraph.edges)
        self.queue = []
        self.stack = []
        self.fingraph = {}
        
    def enqueue(self, node):
        self.queue.append(node)

    def dequeue(self):
        return self.queue.pop(0)

    def push(self, node):
        self.stack.append(node)
    
    def pop(self):
        return self.stack.pop()

    def get_neighbors(self, node):
        if node in self.fingraph:
            return self.fingraph[node]
        else:
            return 
    
    def buildgraph(self):
        for e in self.alledges:
            if e[0] not in self.fingraph:
                self.fingraph[e[0]] = [e[1]]
            else:
                self.fingraph[e[0]].append(e[1])
                
    def bfs(self):
        visited = []
        
        self.enqueue([self.start])
      
        while len(self.queue):
            current_path = self.dequeue()       
            current_vertex = current_path[-1]
            
            if current_vertex == self.targ:
                if self.verbose == "T":
                    return f"{self.fingraph}\n{TYELLOW}{current_path}{ENDC}, {TGREEN}edge found in {len(current_path)}{ENDC} => BFS"
                else:
                    return f"{TYELLOW}{current_path}{ENDC},{TGREEN} edge found in {len(current_path)}{ENDC} => BFS"       
                
            if current_vertex not in visited:
                visited.append(current_vertex)
                
                neighbors = self.get_neighbors(current_vertex)

                if neighbors:
                    for n in neighbors:
                        n_path = list(current_path)
                        n_path.append(n)
                        
                        self.enqueue(n_path)
                        
        if self.verbose == "T":
            return f'{TYELLOW}{self.fingraph}{ENDC}\n{TRED}edge not found => BFS, DFS{ENDC}'
        
        return f'{TRED}edge not found => BFS, DFS{ENDC}'
   
    def dfs(self):
        visited = []
        
        self.push([self.start])
        
        while len(self.stack):
            current_path = self.pop()
            current_vertex = current_path[-1]

            if current_vertex == self.targ:
                return f"{TYELLOW}{current_path}{ENDC},{TGREEN} edge found in {len(current_path)}{ENDC} => DFS"          
                
            if current_vertex not in visited:
                visited.append(current_vertex)
                neighbors = self.get_neighbors(current_vertex)
                
                if neighbors:
                    for n in neighbors:
                        n_path = list(current_path)
                        n_path.append(n)
                        
                        self.push(n_path)
                    
        return ' '
   

if __name__ == '__main__':
    bvd = BFSvsDFS(sys.argv[1:])
    bvd.buildgraph()
    
    print('\n---------------------- BFS v. DFS Time Test ----------------------\n')
    bfs_start_time = time.time()
    print(f"{bvd.bfs()}")
    bfs_end_time = time.time()

    dfs_start_time = time.time()
    print(bvd.dfs())
    dfs_end_time = time.time()
    
    btime = bfs_end_time - bfs_start_time
    dtime = dfs_end_time - dfs_start_time
    
    if btime < dtime:
        print(TGREEN + f"BFS: {bfs_end_time - bfs_start_time}" + ENDC)
        print(TRED + f"DFS: {dfs_end_time - dfs_start_time}" + ENDC)
    else:
        print(TRED + f"BFS: {bfs_end_time - bfs_start_time}" + ENDC)
        print(TGREEN + f"DFS: {dfs_end_time - dfs_start_time}" + ENDC)

    print('\n------------------------------------------------------------------\n')
   