def bfs(graph, start, goal):
   
    visited = []
    queue = [start]
    traversal_path = []

    print("\nBFS Traversal Process")
    while len(queue) > 0:
        current_node = queue.pop(0)
        
        if current_node not in visited:
            visited.append(current_node)
            traversal_path.append(current_node)
            print(f"Visited node: {current_node}")

            if current_node == goal:
                print(f"Goal node '{goal}' found!")
                return traversal_path

            if current_node in graph:
                for neighbor in graph[current_node]:
                    if neighbor not in visited and neighbor not in queue:
                        queue.append(neighbor)

    print(f"Goal node '{goal}' not reachable from start node '{start}'.")
    return traversal_path


def dfs(graph, start, goal):

    visited = []
    stack = [start]
    traversal_path = []

    print("\nDFS Traversal Process")
    while len(stack) > 0:
        
        current_node = stack.pop()

        if current_node not in visited:
            visited.append(current_node)
            traversal_path.append(current_node)
            print(f"Visited node: {current_node}")

            if current_node == goal:
                print(f"Goal node '{goal}' found!")
                return traversal_path

            if current_node in graph:
                neighbors = graph[current_node]
                for i in range(len(neighbors) - 1, -1, -1):
                    neighbor = neighbors[i]
                    if neighbor not in visited:
                        stack.append(neighbor)

    print(f"Goal node '{goal}' not reachable from start node '{start}'.")
    return traversal_path


def main():
    graph = {
        'A': ['C', 'D', 'E'],
        'B': ['F'],
        'C': ['A', 'F'],
        'D': ['A', 'J'],
        'E': ['A', 'J'],
        'F': ['B','C', 'G'],
        'G': ['F', 'H'],
        'H': ['G', 'I'],
        'I': ['H', 'K'],
        'J': ['K','D','E'],
        'K': ['I', 'J', 'L'],
        'L': ['K'],
    }

    print("Adjacency List Graph:")
    for node, neighbors in graph.items():
        print(f"{node}: {neighbors}")

    start_node = input("\nEnter the Start Node: ").upper()
    goal_node = input("Enter the Goal Node: ").upper()

    if start_node not in graph or goal_node not in graph:
        print("Invalid start or goal node entered.")
        return

    bfs_path = bfs(graph, start_node, goal_node)
    print("BFS Path taken:", bfs_path)

    dfs_path = dfs(graph, start_node, goal_node)
    print("DFS Path taken:", dfs_path)


if __name__ == "__main__":
    main()