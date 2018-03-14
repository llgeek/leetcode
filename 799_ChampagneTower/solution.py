from collections import deque


class Solution:
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        glassque = deque()
        glassque.append((0, 0, poured))
        while glassque:
            row, idx, pourednum = glassque.popleft()
            if row == query_row and idx == query_glass:
                return min(pourednum, 1.0)
            if row > 99:
                break
            if pourednum <= 1:
                continue
            overwinbyside = (pourednum-1)*(1/2)
            if glassque:
                endrow, endidx, endpourednum = glassque[-1]
                if endrow == row+1:
                    endrow, endidx, endpourednum = glassque.pop()
                    endpourednum += overwinbyside
                    glassque.append((endrow, endidx, endpourednum))
                else:
                    glassque.append((row+1, idx, overwinbyside))
            else:
                glassque.append((row+1, idx, overwinbyside))
            glassque.append((row+1, idx+1, overwinbyside))
        return 0

s = Solution()
print(s.champagneTower(1000000000, 99, 99))
