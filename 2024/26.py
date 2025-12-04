"""22: monkey market"""
from collections import defaultdict
from functools import reduce
from multiprocessing import Pool
import time
import aocd

MOD_MASK = (1 << 24) - 1
# SEQ_MASK = (1 << 20) - 1

DESIRED_CHUNKS = 8
UNSEEN = 1 << 22

# base-19 I999
SEQ_MAX = 126891
SEQ_SIZE = SEQ_MAX + 1

SLOT_1 = 19 * 19 * 19
SLOT_2 = 19 * 19
SLOT_3 = 19


class Solver():
    def __init__(self, input: str):
        initial_vals = list(map(int, input.strip().split("\n")))

        groups = list(make_groups(initial_vals, DESIRED_CHUNKS))

        self.p2 = 0
        with Pool() as pool:
            res = list(pool.imap_unordered(compute, groups))

            # this is faster than summing an iterator
            self.p1 = res[0][0] + res[1][0] + res[2][0] + res[3][0] + res[4][0] + res[5][0] + res[6][0] + res[7][0]

            for i in range(SEQ_SIZE):
                # this is faster than summing an iterator
                candidate = res[0][1][i] + res[1][1][i] + res[2][1][i] + res[3][1][i] + res[4][1][i] + res[5][1][i] + res[6][1][i] + res[7][1][i]
                self.p2 = max(self.p2, candidate)

    def part_one(self) -> int:
        return self.p1

    def part_two(self) -> int:
        return self.p2


def default():
    return 0


def pool_init():
    global totals

    totals = defaultdict(default)


def compute(values):
    totals = [0] * SEQ_SIZE
    seen = [UNSEEN] * SEQ_SIZE

    num_total = 0

    for i, n in enumerate(values):
        cur = n
        key = 0
        prev_digit = cur % 10

        cur = next_number(cur)
        cur_digit = cur % 10
        prev1 = cur_digit - prev_digit + 9
        prev_digit = cur_digit

        cur = next_number(cur)
        cur_digit = cur % 10
        prev2 = cur_digit - prev_digit + 9
        prev_digit = cur_digit

        cur = next_number(cur)
        cur_digit = cur % 10
        prev3 = cur_digit - prev_digit + 9
        prev_digit = cur_digit

        for j in range(2000 - 3):
            cur = next_number(cur)
            cur_digit = cur % 10
            delta = cur_digit - prev_digit + 9
            # this is faster than the binary approach in rust
            key = prev1 * SLOT_1 + prev2 * SLOT_2 + prev3 * SLOT_3 + delta
            prev_digit = cur_digit

            prev1 = prev2
            prev2 = prev3
            prev3 = delta

            if seen[key] != i:
                seen[key] = i
                totals[key] += cur_digit

        num_total += cur

    return [num_total, totals]


def next_number(input: int) -> int:
    a = input ^ (input << 6) & MOD_MASK
    a = a ^ (a >> 5)
    return a ^ ((a << 11) & MOD_MASK)


def make_groups(a, n):
    k, m = divmod(len(a), n)
    return (a[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n))


def converge(acc, args):
    acc[0] += args[0]
    acc[1] = max(acc[1], args[1])

    for i in range(SEQ_SIZE):
        acc[2][i] += args[2][i]
        acc[1] = max(acc[1], acc[2][i])

    return acc

if __name__ == '__main__':
    START = time.time_ns()
    solver = Solver(aocd.get_data(day=22, year=2024))
    print(solver.part_two())
    print(">>>", (time.time_ns()-START)/1e9)
