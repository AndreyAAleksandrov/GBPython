# for in, map(), filter(), zip()
my_list = [30, 105.6, "text", True]
for e1 in my_list:
    print(e1)

class Iterator:

    def __init__(self, start = 0):
        self.i = start

    def __next__(self):
        self.i +=1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration

class IterObj:

    def __init__(self, start = 0):
        self.start = start -1

    def __iter__(self):
        return Iterator(self.start)


obj = IterObj(start=2)
for e1 in obj:
    print(e1)