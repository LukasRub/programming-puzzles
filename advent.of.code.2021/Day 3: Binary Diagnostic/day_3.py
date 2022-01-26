from collections import Counter
from functools import partial, reduce
from operator import add


INPUT_FILE = "advent.of.code.2021/Day 3: Binary Diagnostic/input.txt"


def read_input(input_file=INPUT_FILE):
    with open(input_file, "rt") as fp:
        return [line.strip() for line in fp]


def task_one(bit_strings):
    # Setting up the counters
    counters = dict.fromkeys(range(len(bit_strings[0])))
    for position in counters.keys():
        counters[position] = Counter()
    
    # Counting bits
    for bit_string in bit_strings:
        for position, bit in enumerate(bit_string):
            counters[position][bit] += 1

    # Counting gamma and epsilon rates
    gamma_rate = int(reduce(add, [counter.most_common()[0][0] for counter in counters.values()]), 2)
    epsilon_rate = int(reduce(add, [counter.most_common()[-1][0] for counter in counters.values()]), 2)

    # Printing results
    print(("gamma rate: {0}; epsilon rate {1}; product {2}"
            .format(gamma_rate, epsilon_rate, gamma_rate*epsilon_rate)))


def xst_common_bit(counter, superlative):
    if superlative == "most":
        return str(int(counter["1"] >= counter["0"]))
    elif superlative == "least":
        return str(int(counter["1"] < counter["0"]))
    

def get_ratings(bit_strings, xst_common_bit_func, position=0):
    # Recursion escape condition
    if len(bit_strings) == 1:
        return bit_strings[0]

    # Counting bits
    counter = Counter()
    for bit_string in bit_strings:
        counter[bit_string[position]] += 1
    
    # Finding superlatives
    flag = xst_common_bit_func(counter)

    # Filtering out bit strings
    bit_strings = [bit_string for bit_string in bit_strings 
                   if bit_string[position] == flag]
    return get_ratings(bit_strings, xst_common_bit_func, position+1)


def task_two(bit_strings):
    oxygen_gen_rating = int(get_ratings(bit_strings, partial(xst_common_bit, superlative="most")), 2)
    co2_scrub_rating = int(get_ratings(bit_strings, partial(xst_common_bit, superlative="least")), 2)

    # Printing results
    print(("Oxygen gen. rating: {0}; CO2 scrub. rating {1}; product {2}"
            .format(oxygen_gen_rating, co2_scrub_rating, oxygen_gen_rating*co2_scrub_rating)))


def main():
    bit_strings = read_input()
    task_one(bit_strings)
    task_two(bit_strings)

if __name__ == "__main__":
    main()