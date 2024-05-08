# Author: Bintang Fajarianto
# Date: May 8 2024

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    last_answer = 0
    
    for op, x, y in queries:
        idx = (x ^ last_answer) % n
        if op == 1:
            arr[idx].append(y)
        elif op == 2:
            last_answer = arr[idx][y % len(arr[idx])]
            yield last_answer