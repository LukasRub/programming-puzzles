import numpy as np

INPUT_FILE = './input.txt'

def map_char_to_int(key):
    str_to_int_map = {'.': 0, '#': 1}
    return str_to_int_map[key]


def read_input(file=INPUT_FILE, print_map=True):
    forest = list()
    with open(INPUT_FILE, 'r') as fp:
        for line in fp.readlines():
            if print_map:
                print(line)
            forest.append(list(map(map_char_to_int, line.strip())))
    forest = np.array(forest)
    return forest


def calculate_step_indices(shape, stride=np.array([1, 3], dtype=np.int8)):
    step_indices = np.ones(((shape[0] - 1) // int(stride[0]) , 2), dtype=np.int8)
    stride = np.array(stride)
    step_indices = np.cumsum(stride * step_indices, axis=0)
    step_indices[:,1] = step_indices[:,1] % shape[1]
    return step_indices


def part_one():
    forest = read_input()
    step_ixs = calculate_step_indices(forest.shape)
    print('Total amount of trees encountered: ',
          forest[tuple(step_ixs.T)].sum())


def part_two():
    forest = read_input()
    strides = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    product = 1
    for stride in strides:
        step_ixs = calculate_step_indices(shape=forest.shape,
                                          stride=stride)
        trees = forest[tuple(step_ixs.T)].sum()
        print(f'{trees} trees enountered with stride {stride}')
        product *= trees
    print('Total product of all trees encountered: ', product)


if __name__ == '__main__':
    # part_one()
    part_two()