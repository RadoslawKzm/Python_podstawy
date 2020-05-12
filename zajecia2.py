import time


# tstart = time.time()
# lst = []
# for i in range(1_000_000):
#     lst.append(i)
# tend = time.time()
# result = tend - tstart
# print(f"funkcja 1 >> {result:0.4f}s")


# tstart = time.time()
# lst3 = [i for i in range(1_000_000)]
# print(f"funkcja 2 >> {time.time() - tstart:0.4f}s")

def choinka():
    rows = 5
    var = rows * 2 + 1
    for row in range(rows):
        print(f"{'*' * (row * 2 + 1):^{var}}")
    return var


test = choinka()


def multiply(a, b):
    var = a * b
    return var


wynik = multiply(1, 2)

"""
0-1     *
1-3    ***
2-5   *****
3-7  *******
"""
"""
0-1 *
1-3 ***
2-5 *****
3-7 *******
"""

"""
for row in range(3)
row = 0
stars = row * 2 + 1
text = row * 2 + 1
print >> |*|

row = 1
stars = row * 2 + 1 =   1 * 2 + 1 = 3
text = row * 2 + 1 =   1 * 2 + 1 = 3
text = |_ _ _|
print >> |***|

|_ _ _ _ _|  << * x1
|_ _ _ _ _|  << * x3
|_ _ _ _ _|  << * x5

|_ _ * _ _|  << * x1
|_ * * * _|  << * x3
|* * * * *|  << * x5

print(f"{'cokolwiek':^}")

|cokolwiek| <>^
|cokolwiek                       | <
|                       cokolwiek| >
|            cokolwiek           | ^

"""
