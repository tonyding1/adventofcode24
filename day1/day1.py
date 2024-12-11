class BaseDay:
    INPUT = 'input.txt'
    OUTPUT = 'output.txt'
    def __init__(self):
        f = open(self.INPUT, 'r')
        self.lines = [line.strip() for line in open(self.INPUT, 'r').readlines()]
    
    def main(self):
        print("one:", self.one())
        print("two:", self.two())

    def one(self):
        return 0
    
    def two(self):
        return 0

class Day(BaseDay):
    def one(self):
        left = []
        right = []
        for line in self.lines:
            tokens = line.split()
            left.append(int(tokens[0]))
            right.append(int(tokens[1]))
        left.sort()
        right.sort()
        sum=0
        for item1,item2 in zip(left, right):
            sum += abs(item1-item2)
        return sum
    
    def two(self):
        left = []
        right = []
        for line in self.lines:
            tokens = line.split()
            left.append(int(tokens[0]))
            right.append(int(tokens[1]))
        left.sort()
        right.sort()
        sum=0
        for item1 in left:
            count = right.count(item1)
            sum += count*item1
        return sum

if __name__ == "__main__":
    day = Day()
    day.main()