#Uses python3

import sys

def innerLoop(s,adj,dist,prev):
    
    for j in range(len(adj)):
        for ind,k in enumerate(adj[j]):
            jkCost = cost[j][ind]
            if dist[k] > dist[j] + jkCost:
                dist[k] = dist[j] + jkCost
                prev[k] = j    

def shortet_paths(adj, cost, s, dist, reachable, shortest, prev):
    #write your code here
    
    #run
    dist[s] = 0  #set origin distance to zero
    
    for i in range(len(adj)-1):   #do this V times total
        innerLoop(s,adj,dist,prev)
    dist_Vminus1 = list(dist)
    #run twice more
    innerLoop(s,adj,dist,prev)     

    dist_V = list(dist)
             
    #find end nodes on negative cycle by finding which ones changes on the last iteration
    changed = [i for i,val in enumerate(dist_Vminus1) if val != dist_V[i]]   
    #find some vertexes on the cycle by following it back in 'prev' V times    
    for i in changed:
        nextV = i
        # Changed vertices are on negative cycles and so have -infinity short path (no shortest path)
        shortest[nextV] = 0
        #follow node back V times.   all along the way will be on shortest path
        for j in range(len(adj)):
            nextV = prev[nextV]
            shortest[nextV] = 0
        shortest[nextV] = 0
        #now move back around cycle until repeats to get remaining vertices
        y = nextV
        while True:
            nextV = prev[nextV]
            if nextV == y:
                break
            shortest[nextV] = 0
            
            
        
                    
    for ind,i in enumerate(dist):
        if i == float('inf'):
            reachable[ind] = 0
        else:
            reachable[ind] = 1
    pass


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s = data[0]
    s -= 1
    dist = [float('inf')] * n
    reachable = [0] * n
    prev      = [-1] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, dist, reachable, shortest, prev)

    
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(dist[x])

