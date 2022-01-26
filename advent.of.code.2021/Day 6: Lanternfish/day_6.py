from functools import partial
import numpy as np


INPUT_FILE = "advent.of.code.2021/Day 6: Lanternfish/input.txt"


def read_input(input_file=INPUT_FILE):
    with open(input_file, "rt") as fp:
        return np.array([int(day) for day in fp.readline().strip().split(",")])


def task_one(initial_state, maximum_days=80, life_cycle=8, reset_to=6):
    print("Initial state:", initial_state)
    current_state = initial_state.copy()

    for day in range(1, maximum_days+1):
        # Count the number of lanternfish that spawn a new fish
        spawn_fish = sum(current_state == 0)

        if spawn_fish > 0:
            # Reset internal time to `reset_to`
            current_state = np.where(current_state == 0, reset_to+1, current_state)
            # Create a new state populated with new lanternfish
            new_state = np.zeros((len(current_state) + spawn_fish, )) + (life_cycle + 1)
            # Copy life cycle data from the current state
            new_state[:len(current_state)] = current_state
            # Reassign `new_state` as the `current_state`
            current_state = new_state

        # Print the status after one day
        current_state -= 1
        print("After {0:3} days: {1}".format(day, current_state))

    print("Total lanternfish after {0} days: {1}".format(day, len(current_state)))


def get_life_cycle_dict(range):
    return {k:0 for k in range}


def task_two(initial_state, maximum_days=18, life_cycle=(8,6)):
    # Freeze args for brevity
    get_life_cycle_dict_ = partial(get_life_cycle_dict, 
                                   range(life_cycle[0]+1)[::-1])

    # Set up initial stade dict
    current_state = get_life_cycle_dict_()

    # Populate `initial_state_` with initial values
    for fish in initial_state:
        current_state[fish] += 1

    print("Initial state: ", current_state)

    # Run simulation
    for day in range(maximum_days):

        # Carry over fish that are about to respawn
        carry_over = get_life_cycle_dict_()
        for c in life_cycle:
            carry_over[c] = current_state[0]

        # Carry over the rest of the fish
        new_state = get_life_cycle_dict_()
        for key in range(1, life_cycle[0]+1):
            new_state[key-1] = current_state[key]

        # Combine carried over states
        for c in life_cycle:
            new_state[c] += carry_over[c]

        # Print new state
        print("After {0:3} days: {1}".format(day+1, sum(new_state.values())))
        current_state = new_state


def main():
    initial_state = read_input()
    task_one(initial_state, maximum_days=80)
    task_two(initial_state, maximum_days=256)


if __name__ == "__main__":
    main()