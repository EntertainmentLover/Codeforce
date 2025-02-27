def main():
    n = int(input())
    if n % 2:
        print(-1)
        return
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    parent = [0]*(n+1)
    order = []
    stack = [1]
    while stack:
        v = stack.pop()
        order.append(v)
        for w in g[v]:
            if w == parent[v]:
                continue
            parent[w] = v
            stack.append(w)
    ans = 0
    sub = [0]*(n+1)
    for v in order[::-1]:
        sub[v] = 1
        for w in g[v]:
            if w == parent[v]:
                continue
            sub[v] += sub[w]
        if v != 1 and sub[v] % 2 == 0:
            ans += 1
    print(ans)
 
main()
