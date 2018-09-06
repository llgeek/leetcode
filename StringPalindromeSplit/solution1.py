"""
memorized iterative code
"""

def memorizedIterativeSplit(s):
    n = len(s)
    M = [[len(s) for _ in range(len(s))] for _ in range(len(s))]
    P = [[-1 for _ in range(len(s))] for _ in range(len(s))]

    for slen in range(1, len(s)+1):
        for i in range(len(s)- slen + 1):
            j = i + slen - 1
            if isPalindrome(s, i, j):
                M[i][j] = 1
                P[i][j] = -1
            else:
                for k in range(i, j):
                    tmpM = M[i][k] + M[k+1][j]
                    if tmpM < M[i][j]:
                        M[i][j] = tmpM
                        P[i][j] = k

    return M[0][len(s)-1], getPalindromeStrings(s, P, 0, len(s)-1)


def isPalindrome(s, i, j):
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    return True


def getPalindromeStrings(s, P, i, j):
    result = []
    if P[i][j] == -1:
        return [s[i:j+1]]
    else:
        result.extend(getPalindromeStrings(s, P, i, P[i][j]))
        result.extend(getPalindromeStrings(s, P, P[i][j]+1, j))
        return result



if __name__ == '__main__':
    s = 'sawiwastoobadihidaboot'
    print(memorizedIterativeSplit(s))
    
