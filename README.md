# BFS-vs-DFS

## INTRODUCTION

The purpose of this short program is to provide the end user with a definitive answer as to which algorithmic search (breadth first, or depth first) is quickest under a given set of circumstances. It first generates a random adjacency matrix using the Erdós-Rényi model. Then `buildgraph()`, a secondary method of the class, converts those edges into an adjacency list for proper traversal of the nodes.

Setting the `verbose` flag to `t` (true) provides the additional benefit of printing out a nice randomized graph in the case you have a need for a quickly and easily generated graph for other applications. It should be noted that depending upon the probability indicated, the generated graph may fall into one or multiple categories, from directed to acyclic to directed acyclic, but is never cyclic or undirected.

<strong>[Coded for use with Python3]</strong>

### DEPENDENCIES

### `networkx (python3 version)`

To install `networkx`, simply type `'pip3 install networkx'` into any open terminal window (requires previous pip installation)

### USAGE

After you've installed `networkx`, run the program using the following command and parameters:

`python3 bfs-vs-dfs.py [n] [p] [s] [t] [v]`

### PARAMETERS

`n` => Number of nodes graph should have (int)  
`p` => Probability for edge creation on each node (float)  
`s` => Start node for search (int)  
`t` => Target node to find in search (int)  
`v` => Verbose output [includes generated graph] (str - t or f)

### USAGE EXAMPLES

<div style="color: orange !important">
python3 bfs-vs-dfs.py 1000 .1 0 290 f<br />
python3 bfs-vs-dfs.py 10 .3 0 5 t  <br />
python3 bfs-vs-dfs.py 75 .7 0 25 t  <br />
python3 bfs-vs-dfs.py 10000 .1 0 2290 f<br />
</div>

### EXAMPLE OUTPUT

```
Standard
---------------------- BFS v. DFS Time Test ----------------------

[0, 10, 290], edge found in 3 => BFS
[0, 270, 280, 290], edge found in 4 => DFS
BFS: 0.007837057113647461
DFS: 0.08036589622497559

------------------------------------------------------------------
```

```
Verbose
---------------------- BFS v. DFS Time Test ----------------------

{0: [2, 3, 4, 5, 7, 8, 9], 1: [3, 4, 5, 6, 7], 2: [4, 5, 6, 8, 9], 3: [5, 9], 4: [5, 6, 9], 5: [6, 7, 8, 9], 6: [7, 8], 7: [8, 9], 8: [9]}

[0, 4], edge found in 2 => BFS
[0, 4], edge found in 2 => DFS
BFS: 2.6702880859375e-05
DFS: 1.9788742065429688e-05

------------------------------------------------------------------

```
