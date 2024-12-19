class BaseDay:
    INPUT = "input.txt"

    def __init__(self):
        f = open(self.INPUT, "r")
        self.lines = [line.strip() for line in open(self.INPUT, "r").readlines()]
        self.rules = []
        self.runs = []
        is_rule = True
        for line in self.lines:
            if not line:
                is_rule = False
                continue
            if is_rule:
                self.rules.append((int(line.split("|")[0]), int(line.split("|")[1])))
            else:
                self.runs.append([int(number) for number in line.split(",")])

    def main(self):
        print("one:", self.one())
        print("two:", self.two())

    def one(self):
        return 0

    def two(self):
        return 0


class Day(BaseDay):
    def is_valid(self, run):
        for rule in self.rules:
            if not self.pass_rule(run, rule): return False
        return True
    def pass_rule(self, run, rule):
        try:
            ele0 = run.index(rule[0])
            ele1 = run.index(rule[1])
            if ele1 < ele0:
                return False
        except ValueError:
            pass
        return True

    def reorder_valid(self, run):
        for rule in self.rules:
            if not self.pass_rule(run, rule):
                # swap
                ele0 = run.index(rule[0])
                ele1 = run.index(rule[1])
                clone = run.copy()
                clone[ele0] = rule[1]
                clone[ele1] = rule[0]
                return self.reorder_valid(clone)
        return run

    def middle_element(self, run):
        index = len(run) // 2
        return run[index]

    def one(self):
        sum = 0
        for run in self.runs:
            if self.is_valid(run):
                sum += self.middle_element(run)
        return sum

    def two(self):
        sum = 0
        for run in self.runs:
            if not self.is_valid(run):
                sum += self.middle_element(self.reorder_valid(run))
        return sum


if __name__ == "__main__":
    day = Day()
    day.main()
