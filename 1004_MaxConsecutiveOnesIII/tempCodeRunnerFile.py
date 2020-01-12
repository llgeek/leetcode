r(acc, start, end, K):
            if start == end:
                return min(1, K)
            if acc[end] - acc[start] + K >= end-start:
                return end-start
            elif start + 1 < end and acc[start] == acc[start+1]:
                    return helper(acc, start+1, end, K)
            elif end - 1 > start and acc[end-1] == acc[end]:
                return helper(acc, start, end-1, K)
            else:
                return max(helper(acc, start+1, end, K), helper(acc, start, end-1, K))