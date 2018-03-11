class MovingAverage(object):
    def __init__(self, size):
        self.stream = []
        self.__size = size
        self.__sum = 0

    def next(self, val):
        if len(self.stream) == self.__size:
            oldval = self.stream.pop(0)
            self.stream.append(val)
            self.__sum = (self.__sum * self.__size - oldval + val) // self.__size
        else:
            oldsize = len(self.stream)
            self.stream.append(val)
            self.__sum = (self.__sum * oldsize + val) / (oldsize + 1)
        return self.__sum

def main():
    a = MovingAverage(3)
    b = [1,2,3,4,5,6,7,8]
    for num in b:
        print(a.next(num))
    # while True:
    #     try:
    #         num = int(input())
    #         print (a.next(int(input())))
    #     except: 
    #         break

if __name__ == '__main__':
    main()


