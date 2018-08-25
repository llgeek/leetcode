import random
class Solutioin:
    def __init__(self, stream, n, k):
        self.stream = stream
        self.n = n
        self.k = k
        self.reservior = []
        self.rnd = random

    def sampleKElements(self):
        self.rnd.seed()
        self.reservior.clear()
        for i in range(self.k):
            self.reservior.append(self.stream[i])
        for i in range(self.k, self.n):
            j = self.rnd.randint(0, i)
            if j < self.k:
                self.reservior[j] = self.stream[i]
        return self.reservior



