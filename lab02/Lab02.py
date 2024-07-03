# 01
import numpy as np
import time

# 02
v = np.array(5)
print(v)

# 03
print(type(v))

# 04
print(v.ndim)

# 05
print(v.shape)
print()

# 06
v = np.array([1, 2, 3, 4, 5, 6])
print(v)
print(v.shape)
print(v.ndim)
print()

# lab07
v = np.array([[1, 2, 3, 4, 5, 6]])
print(v)
print(v.shape)
print(v.ndim)
print()

# 08
u = v.reshape(-1, 1)
print(u)
print(u.shape)
print(u.ndim)
print()

# 09
m = v * u
print(m)
print(m.shape)
print(m.ndim)
print()

# 10
print((v * u == u * v).all())

# 11
print((u @ v == v * u).all())


# 12
def f1(v):
    start = time.time()
    s = sum(v)
    return (time.time() - start)


def f2(v):
    start = time.time()
    s = np.sum(v)
    return (time.time() - start)


# 13
mylist = list(range(1, 1000000))
myarray = np.arange(1, 1000000)

t_lst = 0
t_arr = 0


# for _ in range(1000):
#     t_lst += f1(mylist)
#     t_arr += f2(myarray)
#
# print(f"mylist = {t_lst/1000}")
# print(f"myarray = {t_arr/1000}")
# print()
#
# # 14
# myarray = np.arange(1.0, 1000000.0)
# for _ in range(1000):
#     t_arr += f2(myarray)
#
# print(f"myarray = {t_arr/1000}")
# print()


# 15
def square_num(n):
    return 2 ** (np.arange(1, n))


print(square_num(8))
