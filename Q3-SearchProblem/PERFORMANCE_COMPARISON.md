# Performance Comparison of Search Algorithms

## Comparison Metrics

The comparison was based on the following metrics:

- Solution depth
- Number of nodes expanded
- Execution time

---

## Results from a single execution

| Algorithm | Solution Depth | Nodes Expanded | Time (ms) |
|----------|---------------|---------------|-----------|
| BFS | 11 | 14 | 0.0634 |
| DFS | 11 | 11 | 0.0434 |
| DLS | 11 | 14 | 0.0525 |
| IDS | 11 | 103 | 0.4370 |

---

## Observations

BFS explores the state space level by level and guarantees an optimal solution when step costs are equal. In this problem, BFS expanded 14 nodes before reaching the goal state.

DFS expanded fewer nodes in this execution and completed slightly faster because it explored a branch that directly led to a valid solution. However, DFS does not always guarantee optimality.

DLS is similarl to DFS but restricts the search depth to avoid exploring infinitely deep branches.

IDS repeatedly performs depth-limited searches with increasing depth limits. Because earlier levels are explored multiple times, IDS expanded more nodes and required more time compared to the other algorithms.

---

## Conclusion

All four algorithms successfully found a solution with a depth of 11 moves. In our case, DFS required the fewest node expansions in this specific execution (although BFS is the one that guarantees the optimal solution). IDS combines the advantages of BFS and DFS in theory but resulted in the highest number of node expansions due to repeated searches from the root node in each iteration.
