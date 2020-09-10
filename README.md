# BFS-vs-DFS

## INTRODUCTION

The purpose of this short program is to provide the end user with a definitive answer as to which algorithmic search (breadth first, or depth first) is quickest under a given set of circumstances.

<br />

### DEPENDENCIES

### `networkx (python3 version)`

To install `networkx`, simply type `'pip3 install networkx'` into any open terminal window (requires previous pip installation)

<br />

### USAGE

After you've installed `networkx`, run the program using the following command and parameters:

`python3 bfs-vs-dfs.py [n] [p] [s] [t] [v]`

<br />

### PARAMETERS

`n` => Number of nodes graph should have (int)  
`p` => Probability for edge creation on each node (float)  
`s` => Start node for search (int)  
`t` => Target node to find in search (int)  
`v` => Verbose output [includes generated graph] (str - t or f)

<br />

### USAGE EXAMPLES

<div style="color: orange !important">
python3 bfs-vs-dfs.py 1000 .1 0 290 f<br />
python3 bfs-vs-dfs.py 10 .3 0 5 t  <br />
python3 bfs-vs-dfs.py 75 .7 0 25 t  <br />
python3 bfs-vs-dfs.py 10000 .1 0 2290 f<br />
</div>

<br />

### EXAMPLE OUTPUT

```
---------------------- BFS v. DFS Time Test ----------------------

[0, 10, 290], edge found in 3 => BFS
[0, 270, 280, 290], edge found in 4 => DFS
BFS: 0.007837057113647461
DFS: 0.08036589622497559

------------------------------------------------------------------
```
