

class Guard:
    def __init__(self, row, col, day):
        self.direction = (-1,0)
        self.row = row
        self.col = col
        self.day = day
        self.visited = set()
        self.pos_and_direction = set()
        self.is_looping = False
        # returns (row, col, direction). direction is one of (-1,0),(1,0),(0,-1),(0,1)

    def move(self):
        self.visited.add((self.row, self.col))
        if (self.row, self.col, self.direction) in self.pos_and_direction:
            self.is_looping = True
        self.pos_and_direction.add((self.row, self.col, self.direction))
        next_coord = (self.row+self.direction[0], self.col + self.direction[1])
        next_square = self.day.get(next_coord[0], next_coord[1])
        if next_square is None:
            return False
        elif next_square == self.day.EMPTY or next_square == self.day.GUARD:
            (self.row, self.col) = next_coord
            return True
        elif next_square == self.day.OBSTACLE:
            self.turn_right()
            return True

    
    def turn_right(self):
        if self.direction == (-1,0): 
            self.direction = (0,1)
        elif self.direction == (0,1):
            self.direction = (1,0)
        elif self.direction == (1,0):
            self.direction = (0,-1)
        elif self.direction == (0,-1):
            self.direction = (-1,0)
    

#really should have made a Grid class with a getter and constructor, not a day
class Day:
    INPUT = "input.txt"
    GUARD = '^'
    EMPTY = '.'
    OBSTACLE = '#'

    def __init__(self):
        f = open(self.INPUT, "r")
        self.lines = [line.strip() for line in open(self.INPUT, "r").readlines()]
        self.grid = [list(line) for line in self.lines]
        self.rows = len(self.lines)
        self.cols = len(self.lines[0])

    def main(self):
        print("one:", self.one())
        print("two:", self.two())

    def get(self, row, col):
        if row < 0 or row >= self.rows:
            return None
        if col < 0 or col >= self.cols:
            return None
        return self.grid[row][col]


    def find_guard(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.get(row,col) == self.GUARD:
                    return (row, col)

    def one(self):

        start = self.find_guard()
        guard = Guard(start[0], start[1], self)
        move = guard.move()

        while move:
            move = guard.move()
        
        return len(guard.visited)

    def two(self):
        start = self.find_guard()
        sum = 0
        for row in range(self.rows):
            for col in range(self.cols):
                print(row,col)
                if self.grid[row][col] == self.EMPTY:
                    newday = Day()
                    newday.grid[row][col] = self.OBSTACLE
                    guard = Guard(start[0], start[1], newday)
                    move = guard.move()

                    while move:
                        move = guard.move()
                        if guard.is_looping:
                            print(row,col, "is looping")
                            sum += 1
                            break
    
        return sum


if __name__ == "__main__":
    day = Day()
    day.main()
