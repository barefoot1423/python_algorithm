parent = dict()  # parent pointer
# iterating over the outgoing edges from s
def dfs_visit(s, adj):
    for v in adj[s]:
        if v not in parent:
            parent[v] = s
            dfs_visit(v, adj)
# iterating over the choices of s
def dfs(vertices, adj):
    for s in vertices:
        if s not in parent:
            parent[s] = None
            dfs_visit(s, adj)