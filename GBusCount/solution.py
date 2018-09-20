class GBusCount():
    def gbusCount(self, numofbus, cities, pcity):
        res = {city: 0 for city in pcity}
        for start, end in zip(cities[::2], cities[1::2]):
            

    
    def parse_input(self, inputfile):
        with open(inputfile, 'r') as ff, open('output.txt', 'w') as wf:
            numoftests = int(next(ff))
            for i in range(numoftests):
                numofbus = int(next(ff))
                citystr = next(ff)
                cities = list(map(int, citystr.split(' ')))
                numP = int(next(ff))
                pcity = []
                for k in range(numP):
                    pcity.append(int(next(ff)))
                res = self.gbusCount(numofbus, cities, pcity)
                wf.write('Case #{}:{}\n'.format(i+1, ' '.join(res)))
                next(ff)
