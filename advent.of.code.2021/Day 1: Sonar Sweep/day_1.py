from collections import OrderedDict, Counter


INPUT_FILE = "advent.of.code.2021/Day 1: Sonar Sweep/input.txt"


def read_input(input_file=INPUT_FILE):
    with open(input_file, "rt") as fp:
        return [int(line) for line in fp]


def tag_measurements(depths, window_size=1):
    measurements = OrderedDict.fromkeys(range(len(depths)))
    for i in range(window_size):
        measurements[i] = dict(depth=depths[i]) # initial measurements

    for i, depth in enumerate(depths[window_size:], start=window_size):
        previous_window = sum(depths[i-window_size:i])
        current_window = sum(depths[i-window_size+1:i+1])
        if current_window > previous_window:
            delta = "increased"
        elif current_window < previous_window:
            delta = "decreased"
        else:
            delta = None
        measurements[i] = dict(depth=depth, delta=delta, 
                               current_window=current_window, 
                               previous_window=previous_window)
    
    return measurements


def task_one(depths):
    measurements_w1 = tag_measurements(depths, window_size=1)
    deltas = Counter([measurement["delta"] for measurement 
                      in measurements_w1.values() 
                      if "delta" in measurement.keys()])
    print("Deltas(ws=1)", deltas)


def task_two(depths):
    measurements_w3 = tag_measurements(depths, window_size=3)
    deltas = Counter([measurement["delta"] for measurement 
                      in measurements_w3.values()
                      if "delta" in measurement.keys()])
    print("Deltas(ws=3)", deltas)


def main():
    depths = read_input()
    task_one(depths)
    task_two(depths)

if __name__ == "__main__":
    main()