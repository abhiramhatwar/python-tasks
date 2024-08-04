import sys

def get_ans(N, M, cols, X, edges):
    from collections import defaultdict
    import heapq
    
    adj = defaultdict(list)
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    def dijkstra(src):
        dist = [-float('inf')] * (N + 1)
        dist[src] = 0
        pq = [(-0, src)]
        while pq:
            d, u = heapq.heappop(pq)
            d = -d
            if d < dist[u]:
                continue
            for v, w in adj[u]:
                if dist[v] < d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (-(d + w), v))
        return max(dist)
    
    longest_path = max(dijkstra(i) for i in range(1, N + 1))
    
    expected_longest_path = 0
    for i in range(1, X + 1):
        expected_longest_path += (longest_path + i)
    expected_longest_path /= X
    
    return int(expected_longest_path % (10**9 + 7))

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    M = int(data[index])
    index += 1
    cols = int(data[index])
    index += 1
    X = int(data[index])
    index += 1
    
    edges = []
    for _ in range(M):
        edge = list(map(int, data[index:index + cols]))
        edges.append(edge)
        index += cols
    
    result = get_ans(N, M, cols, X, edges)
    print(result)

if __name__ == "__main__":
    main()