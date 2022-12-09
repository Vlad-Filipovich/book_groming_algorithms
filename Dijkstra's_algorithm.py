graph = {}
graph['start'] = {}
graph['start']['A'] = 6
graph['start']['B'] = 2
graph['A'] = {}
graph['A']['end'] = 1
graph['B'] = {}
graph['B']['A'] = 3
graph['B']['end'] = 5
graph['end'] = {}

# print(graph['start'])
# print(graph['A'])
# print(graph['B'])

infinity = float('inf')
costs = {}
costs['A'] = 6
costs['B'] = 2
costs['end'] = infinity

parents = {}
parents['A'] = 'start'
parents['B'] = 'start'
parents['end'] = None

processed = []


def find_lower_cost_node(costs):
    lower_cost = float('inf')
    lower_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lower_cost and node not in processed:
            lower_cost = cost
            lower_cost_node = node
    return lower_cost_node


node = find_lower_cost_node(costs)
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lower_cost_node(costs)

print(graph)
print(costs)
print(parents)