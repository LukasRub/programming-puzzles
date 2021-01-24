import csv
import numpy as np
import pandas as pd


def read_names(file):
    with open(file, 'r', newline='') as fp:
        for row in csv.reader(fp):
            return pd.Series(np.sort(np.array(row, dtype=np.str_)))


def score(name, shift=-64):
    return sum([ord(c) + shift for c in name])


def main():
    name_series = read_names('project.euler/problem_22/p022_names.txt')
    name_score = (name_series.apply(score) * (name_series.index + 1)).values.sum()
    print(name_score)


if __name__ == '__main__':
    main()