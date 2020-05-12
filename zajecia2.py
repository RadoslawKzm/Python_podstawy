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


for row in range(8):
    print(f"{'*'*(row*2+1):^10}")

"""
0-1     *
1-3    ***
2-5   *****
3-7  *******
"""

