
class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        def valid(S, start, end):
            for i in range(start, end+1):
                if len(chartoidx[S[i]]) > 1 and chartoidx[S[i]][1] > end:
                    return valid(S, i, chartoidx[S[i]][1])
            return end

        chartoidx = dict()
        for i, c in enumerate(S):
            if c not in chartoidx:
                chartoidx[c] = [i]
            elif len(chartoidx[c]) == 2:
                chartoidx[c][-1] = i 
            else:
                chartoidx[c].append(i)
        ret = []
        i = 0
        while i < len(S):
            end = valid(S, i, chartoidx[S[i]][0])
            ret.append(end-i + 1)
            i = end + 1
        return ret

if __name__ == "__main__":
    S = "ababcbacadefegdehijhklij"
    sol = Solution()
    print(sol.partitionLabels(S))

        
