# Missionaries & Cannibals — Search Solver

A Python implementation of the classic **Missionaries and Cannibals** river-crossing problem, solved using four uninformed search algorithms. Built as a clean, readable demonstration of fundamental AI search strategies.

---

## The Problem

Three missionaries and three cannibals need to cross a river. There's one boat that can carry **at most two people**. The catch:

> At no point can cannibals outnumber missionaries on either side of the river — unless there are no missionaries on that side at all.

The goal is to get everyone safely across.

**State representation:** `(missionaries_left, cannibals_left, boat_side)`
- `boat_side = 0` → boat is on the left bank
- `boat_side = 1` → boat is on the right bank

---

## Algorithms

- **BFS (Breadth-first Search)** — explores level by level, guaranteed to find the shortest path
- **DFS (Depth-first Search)** — dives deep before backtracking, memory-efficient but not optimal
- **DLS (Depth Limited Search)** — DFS with a hard depth cap, useful when you have a rough idea of solution depth
- **IDS (Iterative Deepening Search)** — runs DLS with an increasing limit, getting the best of both BFS and DFS

---

**Requirements:** Python 3.7+

```bash
# clone the repo
git clone https://github.com/your-username/missionaries-cannibals.git
cd missionaries-cannibals

# run it
python missionaries_cannibals.py
```

---

## Sample Output

```
╔══════════════════════════════════════════════════════╗
║       Missionaries & Cannibals — Search Solver       ║
╚══════════════════════════════════════════════════════╝

Goal: Move all 3 missionaries and 3 cannibals from
      the left bank to the right bank without letting
      cannibals outnumber missionaries on either side.

───────────────────────────────────────────────────────
  Breadth-First Search (BFS)
───────────────────────────────────────────────────────
  Result  : Solution found ✓
  Depth   : 11 moves
  Nodes   : 15 expanded
  Time    : 0.0821 ms

  Step-by-step path:
  Start →  Left [M:3 C:3] ← Boat  Right [M:0 C:0]
  Step  1 →  Left [M:3 C:1] → Boat  Right [M:0 C:2]
  Step  2 →  Left [M:3 C:2] ← Boat  Right [M:0 C:1]
  ...
  Goal  →  Left [M:0 C:0] → Boat  Right [M:3 C:3]
```

---

## Project Structure

```
Q3-SearchProblem/
└── search.py   
└── README.md
```

