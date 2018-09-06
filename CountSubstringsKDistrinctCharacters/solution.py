"""
assume all characters are between 'a' to 'z' for simplicity
"""

def kDistinctChars(s, k):
    M = [[0 for _ in range(len(s))] for _ in range(len(s))]
    result = 0
    if k > len(s):
        return 0
    for i in range(len(s)):
        M[i][i] = 1 << (ord(s[i]) - ord('a'))
    for slen in range(2, len(s)+1):
        for i in range(0, len(s)-slen+1):
            j = i + slen - 1    
            M[i][j] = M[i][j-1] | 1 << (ord(s[j]) - ord('a'))
    # print(M)
    for slen in range(k, len(s)+1):
        for i in range(0, len(s) - slen + 1):
            if bin(M[i][i+slen-1]).count('1') == k:
                result += 1
    return result

if __name__ == '__main__':
    s = 'aba'
    k = 2
    print(kDistinctChars(s, k))
