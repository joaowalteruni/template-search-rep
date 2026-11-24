from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit
def search(self, initial: State) -> SearchResult:

    frontier = [(initial, 0)]
    visited = {initial}

    nodes_expanded = 0
    nodes_generated = 1
    max_frontier_size = 1

    while frontier:

        current, depth = frontier.pop()
        nodes_expanded += 1

        if current.is_goal:
            return SearchResult(
                solution=current,
                nodes_expanded=nodes_expanded,
                nodes_generated=nodes_generated,
                max_frontier_size=max_frontier_size,
                depth=current.cost
            )

        if depth < self.depth_limit:

            for neighbor in reversed(current.neighbors()):

                if neighbor not in visited:
                    visited.add(neighbor)
                    frontier.append((neighbor, depth + 1))
                    nodes_generated += 1

        max_frontier_size = max(max_frontier_size, len(frontier))

    return SearchResult(
        solution=None,
        nodes_expanded=nodes_expanded,
        nodes_generated=nodes_generated,
        max_frontier_size=max_frontier_size
    )
