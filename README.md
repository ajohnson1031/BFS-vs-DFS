# BFS-vs-DFS

## INTRODUCTION

The purpose of this short program is to provide the end user with a definitive answer as to which algorithmic search (breadth first, or depth first) is quickest under a given set of circumstances. [Made for Python3]

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

{0: [9, 15, 23, 32, 44, 48, 51, 55, 62], 1: [7, 12, 13, 30, 34, 44, 60, 65], 2: [8, 11, 18, 20, 44, 45, 46], 3: [55, 56, 58, 66], 4: [18, 35, 43, 55, 58, 62, 67], 5: [28, 38, 39, 43, 47], 6: [10, 11, 15, 19, 21, 40, 62, 65], 7: [15, 46, 52, 64, 68], 8: [19, 20, 23, 37, 42, 44, 61, 69], 9: [14, 16, 20, 30, 31, 41, 55], 10: [35, 37], 11: [30, 42, 47, 56], 12: [22, 24, 36, 41, 43, 66], 13: [19, 28, 38, 46, 52, 57, 68, 69], 14: [21, 29, 49, 59], 15: [17, 28, 33, 36, 40, 47, 49, 50, 66], 16: [21, 31, 37, 39, 43, 57, 61, 63, 67], 17: [21, 27, 39, 53], 18: [20, 35, 36, 38, 39, 45, 52, 65, 69], 19: [28, 41, 50, 51, 56, 58], 20: [27, 40, 46, 59], 21: [22, 31, 39, 44, 51, 58], 22: [32, 40, 41, 49, 54], 23: [26, 52, 54], 24: [37, 43, 44, 59, 69], 25: [35, 43, 47, 49, 51, 65], 26: [29, 32, 36, 44, 52, 69], 27: [38, 49, 67], 28: [39, 40], 29: [42, 52], 30: [36, 41, 43, 59, 61, 62], 31: [36, 41, 52, 67], 32: [43, 51, 52, 54, 64, 69], 33: [37, 56, 60], 34: [42, 44, 51, 60, 61, 62], 35: [38, 42, 54, 56, 63, 69], 36: [45, 52, 58, 59], 37: [49], 38: [47, 55, 67], 39: [54, 55, 58, 59, 66, 67], 40: [41, 44, 49, 51, 60], 41: [48, 50, 68], 42: [47, 52, 55, 61, 67, 69], 43: [46, 50, 52, 62], 45: [47], 48: [51, 60, 62, 69], 50: [64, 66], 51: [52, 69], 52: [57, 58], 53: [57, 67, 69], 55: [61], 56: [64], 57: [64], 58: [67], 59: [60, 61], 60: [68], 61: [62], 62: [64, 69], 65: [69], 66: [68]}
[0, 9, 14, 29], edge found in 4 => BFS
[0, 23, 26, 29], edge found in 4 => DFS
BFS: 0.0002841949462890625
DFS: 7.081031799316406e-05

------------------------------------------------------------------
```
