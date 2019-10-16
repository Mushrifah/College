def bfs(graph, root, goal):
    queue = []
    path = []
    queue.append(graph[root])
    while (len(queue) != 0):
        current = queue.pop(0)
        path.append(current)
        if( current == goal):
            return ("Found", path)
        else:
            if current in graph.keys():
                temp = graph[current]
                for i in temp:
                    queue.append(i)
    return ("Not found", path)
if __name__ == '__main__':
        graph = {0: 9, 9: [7, 3],
                 7: [5, 1], 3: [2, 4]}
        print("Graph is:",graph)
        print("To find 1")
        res, path = bfs(graph, 0, 1)
        print(res)
        print("Path is:",path)
        print("N = 7 , b = 2 , d = 2")
        print("Space Complexity = O(", len(path) - 1, ")")
        print("Time Complexity = O(", len(path) - 1, ")")

"""
Graph is: {0: 9, 9: [7, 3], 7: [5, 1], 3: [2, 4]}
To find 1
Found
Path is: [9, 7, 3, 5, 1]
N = 7 , b = 2 , d = 2
Space Complexity = O( 4 )
Time Complexity = O( 4 )
"""
