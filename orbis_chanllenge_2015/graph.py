__author__ = 'Qmyang'

__author__ = 'Qmyang'

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

class Arbitrary_object():
    def __init__(self, key):
        self.key = key;


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

def generate_graph_dict(graph):
    new_dict = {}
    for key in graph:
        new_dict[key] = Arbitrary_object(key);
    return new_dict

def generate_x_by_y_graph(x, y):
    new_graph = {}
    if x <= 0 or y <= 0:
        return None
    elif x == 1 and y == 1:
        new_graph[x - 1,y - 1] = None
        return new_graph
    elif x == 1 and y > 1:
        new_graph[0,0] = set([0,1])
        new_graph[0,y - 1] = set([0, y - 2])
    elif x > 1 and y == 1:
        new_graph[0,0] = set([1,0])
        new_graph[x - 1,0] = set([x - 2, 0])
    else:
        new_graph = {(0,0): set([(1,0), (0,1), (1,1)]),
                    (x  - 1,0): set([(x - 2,0), (x - 1,1), (x - 2, 1)]),
                    (0,y - 1): set([(1,y - 1), (0, y - 2), (1,y - 2)]),
                    (x - 1,y - 1): set([(x - 2, y - 1), (x - 1, y - 2), (x - 2, y - 2)])}

    for i in range(1, x - 1):
        new_graph[i,0] = set([(i - 1, 0), (i + 1, 0), (i,1), (i - 1, 1), (i + 1, 1)])
        new_graph[i,y - 1] =  set([(i - 1, y - 1), (i + 1, y - 1), (i,y - 2), (i - 1, y - 2), (i + 1, y - 2)])

    for i in range(1, y - 1):
        new_graph[0,i] = set([(0,i - 1), (0, i + 1), (1,i), (1, i - 1), (1, i + 1)])
        new_graph[x - 1,i] =  set([(x - 1,i - 1), (x - 1, i + 1), (x - 2,i), (x - 2, i - 1), (x - 2, i + 1)])

    for i in range (1, x - 1):
        for j in range (1, y - 1):
            new_graph[i, j] = set([(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1), (i + 1, j + 1)])

    return new_graph


print list(bfs_paths(graph, 'A', 'F'))

test_map = generate_x_by_y_graph(4, 5)
for key in test_map:
    print key
print shortest_path(test_map,(0,0), (3,4))
