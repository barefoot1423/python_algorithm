# s_ -> Node
# adj_ -> adjacent list
def bfs(s, adj):
    level = {s: 0}              # levels
    parent = {s: None}          # parent pointers

    i = 1                       # level
    frontier = [s]              # level i-1

    while frontier:
        _next = list()          # level i
        for u in frontier:
            for v in adj[u]:    # u -> v
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    _next.append(v)

        frontier = _next
        i += 1