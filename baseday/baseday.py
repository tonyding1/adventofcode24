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

if __name__ == "__main__":
    day = Day()
    day.main()