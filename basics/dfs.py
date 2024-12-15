def dfs(graph, start, visited=None):
    """
    DFS is an algorithm for traversing or searching tree or graph data structures.
    The algorithm starts at the root node (selecting some arbitrary node as the root
    in the case of a graph) and explores as far as possible along each branch before backtracking.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for node in graph[start]:
        if node not in visited:
            dfs(graph, node, visited)

if __name__ == "__main__":
    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "F"],
        "F": ["C", "E"],
    }

    dfs(graph, "A")