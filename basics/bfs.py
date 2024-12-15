from collections import deque

def bfs(graph, start):
    """
    BFS is an algorithm for traversing or searching tree or graph data structures. 
    It starts at the tree root (or some arbitrary node of a graph) and explores 
    the neighbor nodes at the present depth level before moving on to nodes at the next depth level.
    """
    visited = set()
    q = deque([start])

    visited.add(start)

    while q:
        node = q.popleft()
        print(node, end=" ")
        for neighbor in graph[node]:
            if neighbor not in visited:
                q.append(neighbor)
                visited.add(neighbor)

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    bfs(graph, "A")