import re


class BaseDay:
    INPUT = "input.txt"
    OUTPUT = "output.txt"

    def __init__(self):
        f = open(self.INPUT, "r")
        self.lines = [line.strip() for line in open(self.INPUT, "r").readlines()]

    def main(self):
        print("one:", self.one())
        print("two:", self.two())

    def one(self):
        return 0

    def two(self):
        return 0


class Day(BaseDay):
    REGEX = "mul\((\d{3}|\d{2}|\d{1}),(\d{3}|\d{2}|\d{1})\)"
    REGEX2 = "(mul\((\d{3}|\d{2}|\d{1}),(\d{3}|\d{2}|\d{1})\)|do\(\)|don't\(\))"

    def one(self):

        sum = 0
        for line in self.lines:
            matches = re.findall(self.REGEX, line)
            for tup in matches:
                sum += int(tup[0]) * int(tup[1])
        return sum

    def two(self):
        sum = 0
        on = True
        for line in self.lines:
            matches = re.findall(self.REGEX2, line)
            for match in matches:
                if match[0] == "don't()":
                    on = False
                elif match[0] == "do()":
                    on = True
                if on and match[0][0] == "m":
                    sum += int(match[1]) * int(match[2])

        return sum


if __name__ == "__main__":
    day = Day()
    day.main()
