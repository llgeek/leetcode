class Solution:
    def camelMatch(self, queries, pattern: str):
        def ifmatch(query, pattern):
            def uppernum(x): return len(list(filter(str.isupper, x)))
            if len(query) < len(pattern) or uppernum(query) > uppernum(pattern):
                return False
            i, j = 0, 0
            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].isupper():
                    return False
                else:
                    i += 1
            if j != len(pattern):
                return False
            if i < len(query) and any(filter(str.isupper, query[i:])):
                return False
            return True
        return [ifmatch(query, pattern) for query in queries]

if __name__ == "__main__":
    queries = ["FooBar", "FooBarTest", "FootBall",
               "FrameBuffer", "ForceFeedBack"]
    pattern = "FB"
    sol = Solution()
    print(sol.camelMatch(queries, pattern))
