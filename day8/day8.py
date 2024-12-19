import itertools
import math
class Day:
    INPUT = "input.txt"

    def __init__(self):
        f = open(self.INPUT, "r")
        self.lines = [line.strip() for line in open(self.INPUT, "r").readlines()]
        self.grid = Grid(self.lines)

    def main(self):
        print("one:", self.one())
        print("two:", self.two())

    def one(self):
        all_nodes = self.grid.get_all_antinodes()
        return len(all_nodes)

    def two(self):
        all_nodes = self.grid.get_all_antinodes(True)
        return len(all_nodes)

class Grid:
    def __init__(self, lines):
        self.grid = [list(line) for line in lines]
        self.rows = len(lines)
        self.cols = len(lines[0])
        self.antennas = {}
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != '.':
                    self.antennas[self.grid[row][col]] = self.antennas.get(self.grid[row][col], []) + [(row,col)]

    def get_all_antinodes(self, just_in_line = False):
        all_antinodes = set()
        for antenna_char in self.antennas:
            all_antinodes.update(self.get_antinodes_for_char(antenna_char, just_in_line))
        return all_antinodes



    def get_antinodes_for_char(self, antenna_char, just_in_line = False):
        if antenna_char not in self.antennas:
            return set()
        antenna_locs = self.antennas[antenna_char]
        choose_two_combos = list(itertools.combinations(antenna_locs,2))
        antinodes = set()
        for (ant1, ant2) in choose_two_combos:
            antinodes.update(self.get_antinodes_for_ant(ant1, ant2, just_in_line))
        return antinodes

    def get_antinodes_for_ant(self, ant1, ant2, just_in_line = False):
        antinodes = set()
        for row in range(self.rows):
            for col in range(self.cols):
                pos = (row,col)
                if just_in_line:
                    if self.in_line(pos,ant1,ant2):
                        antinodes.add(pos)
                else:
                    if self.in_line(pos, ant1, ant2) and  (self.distance(pos, ant1) == 2*self.distance(pos, ant2) or self.distance(pos, ant2) == 2*self.distance(pos, ant1)):
                        antinodes.add(pos)
        return antinodes

    def distance(self, pos1, pos2):
        return math.sqrt((pos1[0]-pos2[0])**2 + (pos1[1]-pos2[1])**2)
    
    def in_line(self, pos, ant1, ant2):
        if pos == ant1 or pos == ant2:
            return True
        if pos[1] == ant1[1] or pos[1] == ant2[1]: #same col
            return ant2[1] == ant1[1]

        slope1 = (pos[0]-ant1[0])/(pos[1]-ant1[1])
        slope2 = (pos[0]-ant2[0])/(pos[1]-ant2[1])
        return slope1 == slope2



        


if __name__ == "__main__":
    day = Day()
    day.main()
