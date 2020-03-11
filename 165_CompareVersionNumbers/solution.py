class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        if not version1:
            return -1 if version2 else 0
        if not version2:
            return 1
        v1 = version1.split('.')
        v2 = version2.split('.')
        minlen = min(len(v1), len(v2))
        for i in range(minlen):
            n1, n2 = v1[i], v2[i]
            n1 = n1.lstrip('0')
            n2 = n2.lstrip('0')
            if n1 == n2:
                continue
            n1 = n1 if n1 else '0'
            n2 = n2 if n2 else '0'
            if int(n1) > int(n2):
                return 1
            else:
                return -1
        j = minlen
        while j < len(v1):
            n1 = v1[j].lstrip('0')
            if n1:
                return 1
            j += 1
        j = minlen
        while j < len(v2):
            n2 = v2[j].lstrip('0')
            if n2:
                return -1
            j += 1
        return 0


if __name__ == "__main__":
    sol = Solution()
    version1 = "1.01"
    version2 = "1.001"
    print(sol.compareVersion(version1, version2))