from collections import deque
class MovingAverage(object):
    def __init__(self, windowsize):
        self.windowsize = windowsize
        self.queue = deque()
        self.avg = 0
    
    def next(self, num):
        if len(self.queue) == self.windowsize:
            oldval = self.queue.popleft()
            self.avg = self.avg + (num - oldval) / self.windowsize
            self.queue.append(num)
        else:
            self.avg = (self.avg * len(self.queue) + num) / (len(self.queue) + 1)
            self.queue.append(num)
        return self.avg


def main():
    a = MovingAverage(3)
    b = [1, 2, 3, 4, 5, 6, 7, 8]
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
