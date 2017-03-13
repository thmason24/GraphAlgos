#Uses python3

import sys
import heapq


def distance(adj, cost, sumCost,s, t):
    #write your code here
    dist = [sumCost+1]*len(adj)
    dist[s] = 0
    prev = [-1]*len(adj)
    h = list(zip(dist,range(len(dist))))
    heapq.heapify(h)
    while len(h) > 0:
        u = heapq.heappop(h)
        for ind,i in enumerate(adj[u[1]]):
            if dist[i] > u[0] + cost[u[1]][ind]:
                dist[i] = u[0] + cost[u[1]][ind]
                prev[i] = u[1]
                heapq.heappush(h,(dist[i],i))
    if dist[t] == sumCost + 1:
        return -1
    else:
        return dist[t]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    sumCost = 0
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
        sumCost += w
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, sumCost, s, t))
