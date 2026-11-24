import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class AStar(BaseSearch):
def heuristic(self, state: State) -> int:

    total = 0

    for value in range(1, 9):

        current_index = state.tiles.index(value)
        goal_index = value - 1

        r1, c1 = divmod(current_index, 3)
        r2, c2 = divmod(goal_index, 3)

        total += abs(r1 - r2) + abs(c1 - c2)

    return total
def search(self, initial: State) -> SearchResult:

    frontier = []
    heapq.heappush(frontier, (self.heuristic(initial), initial))

    visited = set()

    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:

        _, current = heapq.heappop(frontier)

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        if current.is_goal:
            return SearchResult(
                solution=current,
                nodes_expanded=nodes_expanded,
                nodes_generated=nodes_generated,
                max_frontier_size=max_frontier_size,
                depth=current.cost
            )

        for neighbor in current.neighbors():

            if neighbor not in visited:

                priority = neighbor.cost + self.heuristic(neighbor)
                heapq.heappush(frontier, (priority, neighbor))
                nodes_generated += 1

        max_frontier_size = max(max_frontier_size, len(frontier))

    return SearchResult(
        solution=None,
        nodes_expanded=nodes_expanded,
        nodes_generated=nodes_generated,
        max_frontier_size=max_frontier_size
    )
