import numpy as np


INPUT_FILE = "advent.of.code.2021/Day 7: The Treachery of Whales/input.txt"


def read_input(input_file=INPUT_FILE):
    with open(input_file, "rt") as fp:
        return np.array([int(pos) for pos in fp.readline().strip().split(",")])


def task_one(positions):
    possible_range = np.arange(np.min(positions), np.max(positions)+1)
    distances = np.zeros((len(positions), len(possible_range)))

    for pos in possible_range:
        squared_distances = (positions - pos) ** 2
        distances[:, pos] = np.sqrt(squared_distances)
    
    sum_distances = np.sum(distances, axis=0)
    closest_position = np.argmin(sum_distances)
    
    print("Align at {0} with cost of {1}".format(closest_position, 
                                                 sum_distances[closest_position]))


def task_two(positions):
    possible_range = np.arange(np.min(positions), np.max(positions)+1)
    possible_costs = np.cumsum(possible_range)
    costs = np.zeros((len(positions), len(possible_range)))

    for pos in possible_range:
        distances = np.sqrt((positions - pos) ** 2).astype(int)
        costs[:, pos] = possible_costs[distances]
    
    sum_costs = np.sum(costs, axis=0)
    cheapest_position = np.argmin(sum_costs)
    
    print("Align at {0} with cost of {1}".format(cheapest_position, 
                                                 sum_costs[cheapest_position]))


def main():
    positions = read_input()
    task_one(positions)
    task_two(positions)


if __name__ == "__main__":
    main()