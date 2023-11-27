def my_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


def kata_harf(li):
    katta_harflar = []
    for i in li:
        katta_harflar.append(i.title())

    return katta_harflar
