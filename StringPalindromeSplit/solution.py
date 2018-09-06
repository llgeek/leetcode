"""
unmemorized recursive version
"""

def unmemorizedRecursiveSplit(s):
    return unmemorizedRecursiveSplitHelper(s, 0, len(s)-1)

def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True

def unmemorizedRecursiveSplitHelper(s, i, j):   
    if isPalindrome(s, i, j):
        return 1
    minnum = j - i + 1
    for k in range(i, j):
        minnum = min(minnum, unmemorizedRecursiveSplitHelper(s, i, k) + unmemorizedRecursiveSplitHelper(s, k+1, j))
    return minnum    


if __name__ == "__main__":
    s = 'aswastoobadihidaboot'
    print(unmemorizedRecursiveSplit(s))
