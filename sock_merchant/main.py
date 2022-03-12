from typing import Dict


def sockMerchant(n: int, ar: list[int]) -> int:
    res: Dict[int, int] = {}
    c: int = 0

    for i in ar:
        res[i] = 0

    for y in res:
        for w in ar:
            if w == y:
                res[w] += 1

    for k in res:
        c += res[k] // 2

    return c


if __name__ == "__main__":
    sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20])
