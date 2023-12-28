from itertools import chain, combinations

def generate_power_set(input_set):
    power_set = list(chain.from_iterable(combinations(input_set, r) for r in range(len(input_set) + 1)))
    n= sorted(power_set, key=len, reverse=True)
    return [list(n[i]) for i in range(len(n))]
