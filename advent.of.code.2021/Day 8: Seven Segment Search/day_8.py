

INPUT_FILE = "advent.of.code.2021/Day 8: Seven Segment Search/input.txt"


def read_input(input_file=INPUT_FILE):
    signals = list()
    with open(input_file, "rt") as fp:
        for line in fp:
            sequence_str, output_str = line.split("|")
            sequence = sequence_str.strip().split()
            output = output_str.strip().split()
            signals.append((sequence, output))
    return signals


def task_one(input):
    sum_1478s = 0
    for _, output in input:
        for seg_7_digit in output:
            if len(seg_7_digit) in [2, 3, 4, 7]:
                sum_1478s += 1
    print("Number of seven-segment digits of 1,4,7,8:", sum_1478s)


def task_two(input):
    for seqence, output in input:
        ss_one = find_7seg_one(seqence)

    pass


def main():
    input = read_input()
    task_one(input)
    task_two(input)


if __name__ == "__main__":
    main()
