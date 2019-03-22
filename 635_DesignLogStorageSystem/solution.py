class Solution:
    def __init__(self):
        self.log = {}
        self.gras = ['Year', 'Month', 'Day', 'Hour', 'Minute', 'Second']
        self.idx = [4, 7, 10, 13, 16, 19]

    def put(self, id, timestamp):
        self.log[timestamp] = id


    def gettime(self, time, gra):
        idx = self.idx[self.gras.index(gra)]
        return time[:idx]


    def retrieve(self, s, e, gra):
        """retrieve log id within start time: s and end time e, with granularity gra
        
        Arguments:
            s {[str]} -- [description]
            e {[str]} -- [description]
            gra {[str]} -- [granularity]
        
        return: list of ids
        """
        start = self.gettime(s, gra)
        end = self.gettime(e, gra)
        res = []
        # for key, val in self.log.items():
        #     if start <= key and key <= end:
        #         res.append(val)
        return [val for key, val in self.log.items() if start <= self.gettime(key, gra) <= end]

if __name__ == "__main__":
    sol = Solution()
    sol.put(1, "2017:01:01:23:59:59")
    sol.put(2, "2017:01:01:22:59:59")
    sol.put(3, "2016:01:01:00:00:00")
    print(sol.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year"))
    print(sol.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour"))


