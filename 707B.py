def main():
    from heapq import heappush, heappop
    n, m, k = map(int, input("Города, дороги и склады: ").split())
    g = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v, l = map(int, input("Нумеровка и длина двунаправленной дороги: ").split())
        g[u].append((v, l))
        g[v].append((u, l))
    ware = set(map(int, input("Номера городов, в которых склады с мукой:").split())) if k else set()
    if k == 0 or k == n:
        print(-1)
        return
    INF = 10**18
    d = [INF]*(n+1)
    h = []
    for l in ware:
        d[l] = 0
        heappush(h, (0, l))
    while h:
        dd, u = heappop(h)
        if dd != d[u]:
            continue
        for v, l in g[u]:
            nd = dd + l
            if nd < d[v]:
                d[v] = nd
                heappush(h, (nd, v))
    ans = min((d[i] for i in range(1, n+1) if i not in ware), default=INF)
    print(ans if ans != INF else -1)

main()
