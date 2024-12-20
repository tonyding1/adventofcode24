import itertools
import math
class Day:
    INPUT = "input.txt"

    def __init__(self):
        f = open(self.INPUT, "r")
        self.lines = [line.strip() for line in open(self.INPUT, "r").readlines()]
        memory = Memory(self.lines[0])


    def main(self):
        print("one:", self.one())
        print("two:", self.two())

    def one(self):
        memory = Memory(self.lines[0])
        memory.move_blocks()
        return memory.checksum()

    def two(self):
        memory = Memory(self.lines[0])
        memory.move_blocks2()
        return memory.checksum()

class Memory:
    EMPTY = '.'
    def __init__(self, files):
        self.memory = []
        is_file = True
        index = 0
        for num in list(files):
            num = int(num)
            if is_file:
                for size in range(num):
                    self.memory.append(index)
                index += 1
            else:
                for size in range(num):
                    self.memory.append(self.EMPTY)
            is_file = not is_file
        
    def move_blocks(self):
        left_pointer = 0
        right_pointer = len(self.memory)-1
        while left_pointer < right_pointer:
            if self.memory[left_pointer] != '.':
                left_pointer += 1
                continue
            if self.memory[right_pointer] == '.':
                right_pointer -= 1
                continue
            #left is empty, right is a number
            self.memory[left_pointer] = self.memory[right_pointer]
            self.memory[right_pointer] = '.'

    def move_blocks2(self):
        highest_index = max([int(item) for item in self.memory if item != '.'])
        for index in reversed(range(highest_index+1)):
            self.move_file_index(index)
        
    def move_file_index(self, index):
        #find index in file
        first = self.memory.index(index)
        last = len(self.memory) - 1 - self.memory[::-1].index(index)
        # print("looking for index", index, first, last, len(self.memory))
        length = last-first+1
        left_pointer = 0
        while self.memory[left_pointer:left_pointer+length] != ['.']*length:
            left_pointer += 1
            if left_pointer > first:
                return
        self.memory[left_pointer:left_pointer+length] = self.memory[first:last+1]
        self.memory[first:last+1] = ['.']*length
        #check if theres continuous . starting at left_pointer of length last-first


    def checksum(self):
        sum = 0
        for index, num in enumerate(self.memory):
            if num != '.':
                sum += index*int(num)
        return sum

if __name__ == "__main__":
    day = Day()
    day.main()
