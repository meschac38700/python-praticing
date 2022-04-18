def cub(x: int, y: int, z: int, i: int, j: int, repeat: int = 1) -> list[int]:
    res: list[int] = []
    for n in [x, y, z]:
        res = [*res, *[n] * int((3 * i / j))]
    if repeat / 3 > 1:
        print("--->>>", len([*res, *cub(x, y, z, i, j, repeat=repeat - 1)]))
        return [*res, *cub(x, y, z, i, j, repeat=repeat - 1)]
    return res


def cuboid(x: int, y: int, z: int) -> list[list[int]]:
    res: list[list[int]] = []
    for j, i in enumerate(range(3, 0, -1), start=1):
        res = [*res, cub(x, y, z, i, j, repeat=j * 3)]
    return res


def print_cuboid(list_of_n: list[list[int]]):
    print("-->", list_of_n)
    for n_1, n_2, n_3 in zip(*list_of_n):
        print(n_1, n_2, n_3)


print_cuboid(cuboid(10, 11, 12))
