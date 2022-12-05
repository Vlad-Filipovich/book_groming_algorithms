from collections import deque


def person_is_seller(person):
    return 'm' in person


def mango_seller_search(graph):
    search_queue = deque()
    search_queue += graph[list(graph.keys())[0]]
    verified = []

    while search_queue:
        person = search_queue.popleft()

        if person not in verified:

            if person_is_seller(person):
                return f'{person.capitalize()} is a mango seller!'

            else:
                verified.append(person)
                search_queue += graph[person]

    return False


graph = dict()
graph['you'] = ['alice', 'bob', 'claire']
graph['alice'] = ['peggy']
graph['bob'] = ['anuj', 'peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []

print(mango_seller_search(graph))
