#Uses python3

import sys




#explore for directed graph
def explore(adj,x,visited):
    for i in adj[x]:
        if not visited[i]:
            visited[i] = True
            explore(adj,i,visited)
    return


def acyclic(adj):
    acyclic = 0
    for i in range(len(adj)):
        visited = [False] * len(adj)
        explore(adj,i,visited)
        if visited[i]:
            acyclic = 1
            break
    return acyclic

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
