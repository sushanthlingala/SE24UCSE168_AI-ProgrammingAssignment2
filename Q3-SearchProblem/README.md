# Missionaries & Cannibals — Search Solver

An implementation of the **Missionaries and Cannibals** problem, solved using four uninformed search algorithms - BFS, DFS, DLS and IDS (explained later).

---

## The Problem

Three missionaries and three cannibals need to cross a river. There is a single boat that can carry **at most two people**. The condition is that at no point can cannibals be greater than the missionaries on either side of the river (unless there are no missionaries at all on that side of the river).

The goal is to get everyone safely across.

**State representation:** `(missionaries_left, cannibals_left, boat_side)`
- `boat_side = 0` → boat is on the left bank
- `boat_side = 1` → boat is on the right bank

---

## Algorithms Used

- **BFS (Breadth-first Search)** — explores level by level, guaranteed to find the shortest path
- **DFS (Depth-first Search)** — Backtracks after exploring deepest levels first, not optimal but has higher memory efficiency as compared to BSF
- **DLS (Depth Limited Search)** — DFS with a depth limit, useful when you have a rough idea of solution depth
- **IDS (Iterative Deepening Search)** — runs DLS with an increasing limit, which is essentially combining both DFS and BSF

---

**Requirements:** Python 3.7+

```bash
# clone the repo
git clone https://github.com/sushanthlingala/SE24UCSE168_AI-ProgrammingAssignments
cd Q3-SearchProblem

# run it
python search.py
```

---

## Sample Output

```
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

For detailed algorithm comparison see [PERFORMANCE_COMPARISON.md](PERFORMANCE_COMPARISON.md)

## Project Structure

```
Q3-SearchProblem
├── search.py
├── README.md
└── PERFORMANCE_COMPARISON.md
```

