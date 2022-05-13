from typing import List, Sized

S1 = "13715248055ax5"
S2 = "11145"


def create_table(s1: str, s2: str) -> List[List[int]]:
    n, m = len(s1) + 1, len(s2) + 1

    table = [
        [1 for _ in range(n)] for _ in range(m)
    ]  # fill table by def value

    for i, v in enumerate(s2):
        for j, vv in enumerate(s1):
            if v != vv:
                table[i + 1][j + 1] = max(table[i + 1][j], table[i][j + 1])
            else:
                table[i + 1][j + 1] = table[i][j] + 1

    return table


def print_table(s1: str, s2: str, table: List[List[int]]):
    seq = set()
    for v in table[:-1]:
        max_eq = max(v)
        for i, vv in enumerate(v[:-1]):
            if vv - max_eq == 0:
                seq.add(s1[i - 1])
                break

    print('len=', table[len(s2) - 1][len(s1) - 1])
    print('seq=', seq)

    print('  |', ' '.join(s1))
    print('--|' + '-' * len(S1)*2)

    for i, v in enumerate(s2):
        results = map(str, table[i][:-1])
        print(v, '|', ' '.join(results))


if __name__ == "__main__":
    t = create_table(S1, S2)
    print_table(S1, S2, t)
