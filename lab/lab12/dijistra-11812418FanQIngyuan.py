from numpy import inf

graph = {
    'A': {'E': 3, 'B': 7, 'F': 2, 'D': 3},
    'B': {'E': 1, 'A': 7, 'F': 2, 'C': 5},
    'C': {'B': 5, 'F': 3, 'D': 6},
    'D': {'C': 6, 'F': 1, 'A': 3},
    'E': {'B': 1, 'A': 3},
    'F': {'C': 3, 'D': 1, 'A': 2, 'B': 2}
}

costs = {'A': inf, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}

parents = {}


def search(source, target, graph, costs, parents):
    costs[source] = 0
    nextNode = source

    while nextNode != target:

        for neighbor in graph[nextNode]:

            if graph[nextNode][neighbor] + costs[nextNode] < costs[neighbor]:
                costs[neighbor] = graph[nextNode][neighbor] + costs[nextNode]
                parents[neighbor] = nextNode
            del graph[neighbor][nextNode]
        del costs[nextNode]
        nextNode = min(costs, key=costs.get)
    return parents


# result = search('A', 'C', graph, costs, parents)

def backpedal(source, target, searchResult):
    node = target

    backpath = [target]

    path = []

    while node != source:
        backpath.append(searchResult[node])

        node = searchResult[node]

    for i in range(len(backpath)):
        path.append(backpath[-i - 1])

    return path


# print('parent dictionary={}'.format(result))
#
# print('ideal path={}'.format(backpedal('A', 'C', result)))


def router_table(src, dst):

    costs_tmp = {'A': inf, 'B': inf, 'C': inf, 'D': inf, 'E': inf, 'F': inf}
    graph = {
    'A': {'E': 3, 'B': 7, 'F': 2, 'D': 3},
    'B': {'E': 1, 'A': 7, 'F': 2, 'C': 5},
    'C': {'B': 5, 'F': 3, 'D': 6},
    'D': {'C': 6, 'F': 1, 'A': 3},
    'E': {'B': 1, 'A': 3},
    'F': {'C': 3, 'D': 1, 'A': 2, 'B': 2}
}
    parents = {}
    result = search(src, dst, graph, costs_tmp, parents)
    path = backpedal(src, dst, result)
    next_hop = path
    return next_hop

# print forwarding table
# the value of each key is the link that the packet should go
def print_forward_table(src):
    fwd_table = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
    del fwd_table[src]
    for dst in fwd_table:
        link_array = [src]
        table = router_table(src,dst)
        link_array.append(table[1])
        print(table)
        fwd_table[dst] = link_array
    return fwd_table

print(print_forward_table("A"))