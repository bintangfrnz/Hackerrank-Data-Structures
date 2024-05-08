# Author: Bintang Fajarianto
# Date: May 8 2024

import sys

def hourglassSum(arr):
    max_sum = -sys.maxsize - 1
    for c in range(4):
        for r in range(4):
            c_sum = calculate_hourglass_sum(arr, c, r)
            
            if (c_sum > max_sum):
                max_sum = c_sum
    return max_sum
            
def calculate_hourglass_sum(arr, c, r):
    top = arr[c][r] + arr[c][r+1] + arr[c][r+2]
    mid = arr[c+1][r+1]
    bot = arr[c+2][r] + arr[c+2][r+1] + arr[c+2][r+2]
    return top + mid + bot