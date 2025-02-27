def solve():
    t = int(input("Кол-во наборов: "))
    for _ in range(t):
        n = int(input("Длина массивов: "))
        a = list(map(int, input("Первый массив: ").split()))
        b = list(map(int, input("Второй массив: ").split()))
        X = [a[i] - b[i] for i in range(n)]
        maxX = max(X)
        strong_vertices = [str(i + 1) for i in range(n) if X[i] == maxX]
        print(len(strong_vertices))
        print(" ".join(strong_vertices))

if __name__ == '__main__':
    solve()