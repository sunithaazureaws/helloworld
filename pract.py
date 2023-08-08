def cmp(str1, str2):
    if len(str1) != len(str2):
        return False

    d, d2 = {}, {}
    for char in str1:
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    for char in str2:
        if char not in d:
            return False
        if char not in d2:
            d2[char] = 1
        else:
            d2[char] += 1

    return d == d2
a="abc"
b="cah"
print(cmp(a,b))
