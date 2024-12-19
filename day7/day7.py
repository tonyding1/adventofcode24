class Day:
    INPUT = "input.txt"

    def __init__(self):
        f = open(self.INPUT, "r")
        self.lines = [line.strip() for line in open(self.INPUT, "r").readlines()]
        self.equations = []
        for line in self.lines:
            tokens = line.split(':')
            result = int(tokens[0])
            operands = [int(item) for item in tokens[1].split(' ')[1:]]
            self.equations.append(Equation(result, operands))

    def main(self):
        print("one:", self.one())
        print("two:", self.two())

    def one(self):
        sum = 0
        for equation in self.equations:
            if equation.can_combine():
                sum += equation.result
        return sum

    def two(self):
        sum = 0
        for equation in self.equations:
            if equation.can_combine2():
                sum += equation.result
        return sum


class Equation:

    def __init__(self, result, operands):
        self.result = result
        self.operands = operands

    def can_combine(self):
        #add
        if len(self.operands) == 1:
            return self.result == self.operands[0]
        add_operator_equation = Equation(self.result, [self.operands[0] + self.operands[1]] + self.operands[2:])
        mult_operator_equation = Equation(self.result, [self.operands[0] * self.operands[1]] + self.operands[2:])
        return add_operator_equation.can_combine() or mult_operator_equation.can_combine()

    def can_combine2(self):
        #add
        if len(self.operands) == 1:
            return self.result == self.operands[0]
        add_operator_equation = Equation(self.result, [self.operands[0] + self.operands[1]] + self.operands[2:])
        mult_operator_equation = Equation(self.result, [self.operands[0] * self.operands[1]] + self.operands[2:])
        concat_operator_equation = Equation(self.result, [int(str(self.operands[0]) + str(self.operands[1]))] + self.operands[2:])
        return add_operator_equation.can_combine2() or mult_operator_equation.can_combine2() or concat_operator_equation.can_combine2()

if __name__ == "__main__":
    day = Day()
    day.main()
