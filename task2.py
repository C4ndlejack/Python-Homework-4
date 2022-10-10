def Factor(num):
    list = []
    d = 2
    while d * d <= num:
        if num % d == 0:
            list.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        list.append(num)
    return list
print(Factor(int(input())))

