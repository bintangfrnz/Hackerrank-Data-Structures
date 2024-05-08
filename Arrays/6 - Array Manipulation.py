# Author: Bintang Fajarianto
# Date: May 8 2024

def arrayManipulation(n, queries):
    arr = [0] * n
    for a, b, k in queries:
        arr[a-1] += k
        if b != n:
            arr[b] -= k
    
    max_value = 0
    c_value = 0
    for i in range(n):
        c_value += arr[i]
        if max_value < c_value:
            max_value = c_value
            
    return max_value