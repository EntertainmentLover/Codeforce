def s():
    t = int(input())
    for _ in range(t):
        x = int(input())
        pos = False
        for c in range(0,100):
            if x >= c * 111 and (x - c * 111) % 11 == 0:
                pos = True
                break
        print("YES" if pos else "NO") 

if __name__ == "__main__":
    s()  