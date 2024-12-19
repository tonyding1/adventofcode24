class BaseDay:
    INPUT = "input.txt"

    def __init__(self):
        f = open(self.INPUT, "r")
        self.lines = [line.strip() for line in open(self.INPUT, "r").readlines()]
        self.grid = [list(line) for line in self.lines]
        self.rows = len(self.lines)
        self.cols = len(self.lines[0])
        print(self.grid)

    def main(self):
        print("one:", self.one())
        print("two:", self.two())

    def one(self):
        return 0

    def two(self):
        return 0


class Day(BaseDay):

    def get(self, row, col):
        if row < 0 or row >= self.rows:
            return None
        if col < 0 or col >= self.cols:
            return None
        return self.grid[row][col]

    # num XMAS hits at row, col
    def matches(self, row, col, direction):
        return (
            self.get(row, col) == "X"
            and self.get(row + direction[0], col + direction[1]) == "M"
            and self.get(row + 2 * direction[0], col + 2 * direction[1]) == "A"
            and self.get(row + 3 * direction[0], col + 3 * direction[1]) == "S"
        )

    def total_matches(self, row, col):
        sum = 0
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for direction in directions:
            if self.matches(row, col, direction):
                sum += 1
        return sum

    # num MASMAS hits at row, col
    def matches2(self, row, col):
        return (
            self.get(row, col) == "A"
            and (self.get(row - 1, col - 1), self.get(row + 1, col + 1))
            in [("M", "S"), ("S", "M")]
            and (self.get(row - 1, col + 1), self.get(row + 1, col - 1))
            in [("M", "S"), ("S", "M")]
        )

    def one(self):
        sum = 0
        for row in range(self.rows):
            for col in range(self.cols):
                sum += self.total_matches(row, col)

        return sum

    def two(self):
        sum = 0
        for row in range(self.rows):
            for col in range(self.cols):
                sum += 1 if self.matches2(row, col) else 0

        return sum


if __name__ == "__main__":
    day = Day()
    day.main()
