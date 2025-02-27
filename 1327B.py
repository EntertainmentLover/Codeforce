def solve():
    t = int(input("Количество тестов: "))
    for _ in range(t):
        n = int(input("Количество дочерей и королевств: "))
        married_princes = set()
        unmarried_daughter = -1 
        
        preferences = [] 
        
        for i in range(1, n + 1):
            data = list(map(int, input("Массив: ").split()))
            k = data[0] 
            choices = data[1:] 
            preferences.append(choices)
            married = False 
            for prince in choices:
                if prince not in married_princes:
                    married_princes.add(prince)
                    married = True
                    break
            if not married and unmarried_daughter == -1:
                unmarried_daughter = i 
        if unmarried_daughter == -1:
            print("OPTIMAL")
        else:
            for prince in range(1, n + 1):
                if prince not in married_princes:
                    print("IMPROVE")
                    print(unmarried_daughter, prince)
                    break

if __name__ == "__main__":
    solve()
