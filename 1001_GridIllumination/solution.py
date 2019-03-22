class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        X, Y, EN, WN = {}, {}, {}, {}
        lampset = set()
        for lamp in lamps:
            if lamp[0] not in X:
                X[lamp[0]] = 0
            if lamp[1] not in Y:
                Y[lamp[1]] = 0
            if lamp[1] - lamp[0] not in EN:
                EN[lamp[1] - lamp[0]] = 0
            if lamp[0]+lamp[1] not in WN:
                WN[lamp[0]+lamp[1]] = 0
            X[lamp[0]] += 1
            Y[lamp[1]] += 1
            EN[lamp[1] - lamp[0]] += 1
            WN[lamp[0]+lamp[1]] += 1
            lampset.add((lamp[0], lamp[1]))
        res = []
        dist = {(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0),
                (1, 1), (1, -1), (-1, 1), (-1, -1)}
        for q in queries:
            if q[0] in X or q[1] in Y or q[1]-q[0] in EN or q[0]+q[1] in WN:
                res.append(1)
            else:
                res.append(0)
            for d in dist:
                newx, newy = q[0] + d[0], q[1] + d[1]
                if (newx, newy) in lampset:
                    lampset.discard((newx, newy))
                    X[newx] -= 1
                    Y[newy] -= 1
                    EN[newy-newx] -= 1
                    WN[newx+newy] -= 1
                    if X[newx] == 0:
                        X.pop(newx)
                    if Y[newy] == 0:
                        Y.pop(newy)
                    if EN[newy-newx] == 0:
                        EN.pop(newy-newx)
                    if WN[newx+newy] == 0:
                        WN.pop(newx+newy)
        return res
