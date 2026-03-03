import time
from collections import deque

class MissionariesAndCannibals:
    """
    State: (missionaries_left, cannibals_left, boat_side)
      - missionaries_left : number of missionaries on the left bank (0–3)
      - cannibals_left    : number of cannibals on the left bank (0–3)
      - boat_side         : 0 = boat on left, 1 = boat on right
    """

    TOTAL = 3  

    MOVES = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    def __init__(self):
        self.initial_state = (3, 3, 0)  
        self.goal_state    = (0, 0, 1)  

    def goal_test(self, state):
        return state == self.goal_state

    def is_valid(self, state):
        m_left, c_left, _ = state
        m_right = self.TOTAL - m_left
        c_right = self.TOTAL - c_left

        
        if not (0 <= m_left <= self.TOTAL and 0 <= c_left <= self.TOTAL):
            return False

        
        if m_left > 0 and c_left > m_left:
            return False
        if m_right > 0 and c_right > m_right:
            return False

        return True

    def get_successors(self, state):
        m_left, c_left, boat = state
        successors = []

        for m, c in self.MOVES:
            if boat == 0:   
                new_state = (m_left - m, c_left - c, 1)
            else:           
                new_state = (m_left + m, c_left + c, 0)

            if self.is_valid(new_state):
                successors.append(new_state)

        return successors


def reconstruct_path(parent, goal_state):
    
    path = [goal_state]
    while goal_state in parent:
        goal_state = parent[goal_state]
        path.append(goal_state)
    path.reverse()
    return path


def bfs(problem):
    start_time = time.time()
    frontier = deque([problem.initial_state])
    explored = set()
    parent = {}
    nodes_expanded = 0

    while frontier:
        state = frontier.popleft()

        if problem.goal_test(state):
            path = reconstruct_path(parent, state)
            return path, nodes_expanded, time.time() - start_time

        if state in explored:
            continue

        explored.add(state)
        nodes_expanded += 1

        for child in problem.get_successors(state):
            if child not in explored and child not in frontier:
                parent[child] = state
                frontier.append(child)

    return None, nodes_expanded, time.time() - start_time


def dfs(problem):
    start_time = time.time()
    frontier = [problem.initial_state]
    explored = set()
    parent = {}
    nodes_expanded = 0

    while frontier:
        state = frontier.pop()

        if problem.goal_test(state):
            path = reconstruct_path(parent, state)
            return path, nodes_expanded, time.time() - start_time

        if state in explored:
            continue

        explored.add(state)
        nodes_expanded += 1

        for child in problem.get_successors(state):
            if child not in explored and child not in frontier:
                parent[child] = state
                frontier.append(child)

    return None, nodes_expanded, time.time() - start_time


def depth_limited_search(problem, limit):
    def _recursive_dls(state, limit, parent, explored):
        if problem.goal_test(state):
            return reconstruct_path(parent, state)

        if limit == 0:
            return None  

        explored.add(state)

        for child in problem.get_successors(state):
            if child not in explored:
                parent[child] = state
                result = _recursive_dls(child, limit - 1, parent, explored)
                if result is not None:
                    return result

        return None

    return _recursive_dls(problem.initial_state, limit, {}, set())


def iterative_deepening_search(problem):
    start_time = time.time()
    nodes_expanded = 0  
    depth = 0

    while True:
        result = depth_limited_search(problem, depth)
        if result is not None:
            return result, nodes_expanded, time.time() - start_time
        depth += 1


def format_state(state):
    m_left, c_left, boat = state
    m_right = MissionariesAndCannibals.TOTAL - m_left
    c_right = MissionariesAndCannibals.TOTAL - c_left
    boat_str = "←" if boat == 0 else "→"
    return f"Left [M:{m_left} C:{c_left}] {boat_str} Boat  Right [M:{m_right} C:{c_right}]"


def print_results(name, path, nodes_expanded, elapsed, show_path=True):
    print(f"\n{name}")
    if path is None:
        print("  Result  : No solution found")
    else:
        print(f"  Result  : Solution found ✓")
        print(f"  Depth   : {len(path) - 1} moves")
        if nodes_expanded is not None:
            print(f"  Nodes   : {nodes_expanded} expanded")
        print(f"  Time    : {elapsed * 1000:.4f} ms")

        if show_path:
            print(f"\n  Step-by-step path:")
            for i, state in enumerate(path):
                prefix = "  Start →" if i == 0 else f"  Step {i:>2} →" if i < len(path) - 1 else "  Goal  →"
                print(f"  {prefix}  {format_state(state)}")


if __name__ == "__main__":
    problem = MissionariesAndCannibals()

    path, nodes, elapsed = bfs(problem)
    print_results("Breadth-First Search (BFS)", path, nodes, elapsed)

    path, nodes, elapsed = dfs(problem)
    print_results("Depth-First Search (DFS)", path, nodes, elapsed)

    limit = 12
    start = time.time()
    path = depth_limited_search(problem, limit)
    elapsed = time.time() - start
    print_results(f"Depth-Limited Search (limit = {limit})", path, None, elapsed)

    path, nodes, elapsed = iterative_deepening_search(problem)
    print_results("Iterative Deepening Search (IDS)", path, nodes, elapsed)
