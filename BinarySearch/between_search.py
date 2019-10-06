"""
given sorted list A, find the maximum value that smaller than target
"""

def between_search(A, target):
    start, end = 0, len(A)-1
    while start < end:
        mid = (start + end+1) // 2      ## IMPORTANT!! use ceil instead of floor, to avoid dead loop
        if A[mid] <= target:
            start = mid
        else:
            end = mid-1
    return start if A[start] <= target else -1

print(between_search([1], 0))



"""
given sorted list A, find the minimum value that greater than target
"""
def between_search_v2(A, target):
    start, end = 0, len(A)-1
    while start < end:
        mid = (start+end)//2
        if A[mid] < target:
            start = mid + 1
        else:
            end = mid
    return start if A[start] >= target else -1

print(between_search_v2([0,1], 0))
