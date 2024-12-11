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
    def is_safe(self, tokens):
        if (self.increasing(tokens) or self.decreasing(tokens)) and self.small_steps(tokens):
            return True
        return False


    def increasing(self, tokens):
        return all(i < j for i,j in zip(tokens, tokens[1:]))
    def decreasing(self, tokens):
        return all(i > j for i,j in zip(tokens, tokens[1:]))
    def small_steps(self, tokens):
        diffs = [abs(x - tokens[i-1]) for i, x in enumerate(tokens)][1:]
        return all( (diff >= 1 and diff <= 3 ) for diff in diffs)
    
    def is_mostly_safe(self, tokens):
        for i in range(len(tokens)):
            subtokens = tokens[:i] + tokens[i+1:]
            if self.is_safe(subtokens):
                return True
        return False


    def one(self):
        total_safe = 0
        for line in self.lines:
            tokens = line.split()
            tokens = [int(item) for item in tokens]
            if self.is_safe(tokens):
                total_safe += 1
        return total_safe

    
    def two(self):
        total_safe = 0
        for line in self.lines:
            tokens = line.split()
            tokens = [int(item) for item in tokens]
            if self.is_mostly_safe(tokens):
                total_safe += 1
        return total_safe

if __name__ == "__main__":
    day = Day()
    day.main()