#Uses python3

import sys


def explore(adj,x,visited):
    for i in adj[x]:
        if not visited[i]:
            visited[i] = True
            explore(adj,i,visited)
    return visited

def reach(adj, x, y):
    #write your code here
    #start exploring vertex 1
    visited = [False] * len(adj)
    explore(adj,x,visited)
    if visited[y]:
        return 1
    else:
        return 0

    #return explore(adj,x,visited)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    #print('edges')
    #print(edges)
    #print
    x, y = data[2 * m:]
    #print('x: ' + str(x))
    #print('y: ' + str(y))

    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    #print(adj)
        
    print(reach(adj, x, y))
