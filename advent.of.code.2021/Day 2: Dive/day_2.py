INPUT_FILE = "advent.of.code.2021/Day 2: Dive/input.txt"


class Navigation:
    horizontal_position = 0
    vertical_position = 0
    maneuvers = list()

    def __init__(self, configuration):
        self.configuration = configuration
        if configuration == "task_2":
            self.aim = 0


    def resolve_maneuver(self, maneuver):
        if self.configuration == "task_1":
            if "forward" in maneuver.keys():
                self.horizontal_position += maneuver["forward"]
            if "up" in maneuver.keys():
                self.vertical_position -= maneuver["up"]
            if "down" in maneuver.keys():
                self.vertical_position += maneuver["down"]
                
        elif self.configuration == "task_2":
            if "forward" in maneuver.keys():
                self.horizontal_position += maneuver["forward"]
                self.vertical_position += self.aim * maneuver["forward"]
            if "up" in maneuver.keys():
                self.aim -= maneuver["up"]
            if "down" in maneuver.keys():
                self.aim += maneuver["down"]
        
        self.maneuvers.append(maneuver)


    def __repr__(self):
        return (("Navigation(horizontal_position={0}," +
                    "vertical_position={1}," + 
                    "total_postion={2})")
                    .format(self.horizontal_position, 
                            self.vertical_position,
                            self.horizontal_position * self.vertical_position))


def read_input(input_file=INPUT_FILE):
    lines = list()
    with open(input_file, "rt") as fp:
        for line in fp:
            direction, points = line.split()
            lines.append({direction: int(points)})
    return lines


def task_one(maneuvers):
    navigation = Navigation(configuration="task_1")
    for maneuver in maneuvers:
        navigation.resolve_maneuver(maneuver)
    print(navigation)


def task_two(maneuvers):
    navigation = Navigation(configuration="task_2")
    for maneuver in maneuvers:
        navigation.resolve_maneuver(maneuver)
    print(navigation)


def main():
    maneuvers = read_input()
    task_one(maneuvers)
    task_two(maneuvers)


if __name__ == "__main__":
    main()