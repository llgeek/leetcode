import random
class Solutioin:
    def __init__(self, stream, n, k):
        self.stream = stream
        self.n = n
        self.reservior = []
        self.rnd = random

    def sampleKElements(self):
        self.rnd.seed()

        self.reservior.clear()
        for i in range(k):
            self.reservior.append[stream[i]]
        for i in range(k, self.n):
            j = self.rnd(0, i)
            if j < k:
                self.reservior[j] = self.stream[i]
        return self.reservior



