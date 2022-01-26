import numpy as np


INPUT_FILE = "advent.of.code.2021/Day 5: Hydrothermal Venture/input.txt"


class Point:

    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord


    def dimensions(self):
        return max([self.x_coord, self.y_coord]) + 1

    
    def __eq__(self, other):
        return (self.x_coord == other.x_coord) and (self.y_coord == other.y_coord)


    def __repr__(self):
        return "Point(x={0},y={1})".format(self.x_coord, self.y_coord)


    def __iter__(self):
        yield self.x_coord
        yield self.y_coord

    
    def __gt__(self, other):
        return max([self.x_coord, self.y_coord]) > max([other.x_coord, other.y_coord])


    @classmethod
    def from_other(cls, other):
        return cls(other.x_coord, other.y_coord)


    @classmethod
    def from_string(cls, string):
        return cls(*[int(coord) for coord in string.split(",")])


class Line:

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b


    def points(self):
        yield self.point_a

        new_point = Point.from_other(self.point_a)
        while new_point != self.point_b:
            if new_point.x_coord != self.point_b.x_coord:
                if new_point.x_coord < self.point_b.x_coord:
                    new_point.x_coord += 1
                else:
                    new_point.x_coord -= 1

            if new_point.y_coord != self.point_b.y_coord:
                if new_point.y_coord < self.point_b.y_coord:
                    new_point.y_coord += 1
                else:
                    new_point.y_coord -= 1

            yield new_point
    

    def is_straight(self):
        return (self.point_a.x_coord == self.point_b.x_coord or
                    self.point_a.y_coord == self.point_b.y_coord)

    
    def dimensions(self):
        return max([self.point_a, self.point_b]).dimensions()


    def __iter__(self):
        yield self.point_a
        yield self.point_b


    def __gt__(self, other):
        return max([self.point_a, self.point_b]) > max([other.point_a, other.point_b])


    def __repr__(self):
        return "Line({0})".format(",".join([str(p) for p in self.points()]))
        

class Grid:

    def __init__(self, grid_dimensions=10):
        self._grid = np.zeros((grid_dimensions, grid_dimensions))


    def draw_line(self, line):
        for point in line.points():
            self._grid[point.x_coord, point.y_coord] +=1


    def count_overlaps(self):
        return np.sum(self._grid > 1, axis=(0,1))


    def __repr__(self):
        return str(self._grid.T)


def read_input(input_file=INPUT_FILE):
    lines = list()
    with open(input_file, "rt") as fp:
        for line in fp:
            lines.append(Line(*[Point.from_string(p) for p in line.split(" -> ")]))
    return lines


def task_one(lines):
    grid = Grid(grid_dimensions=max(lines).dimensions())
    for line in lines:
        if line.is_straight():
            grid.draw_line(line)
    # print(grid)
    print("Overlapping points:", grid.count_overlaps())


def task_two(lines):
    grid = Grid(grid_dimensions=max(lines).dimensions())
    for line in lines:
        grid.draw_line(line)
    # print(grid)
    print("Overlapping points:", grid.count_overlaps())


def main():
    lines = read_input()
    task_one(lines)
    task_two(lines)


if __name__ == "__main__":
    main()