def compareTriplets(a: list[int], b: list[int]) -> list[int]:
    cA: int = 0
    cB: int = 0

    for k, _ in enumerate(a):
        if a[k] > b[k]:
            cA += 1
        elif a[k] < b[k]:
            cB += 1

    return [cA, cB]


if __name__ == '__main__':
    print(compareTriplets([3, 5, 1], [6, 2, 1]))
