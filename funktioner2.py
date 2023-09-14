def swapper(a,b):
    return b,a

a = 1
b = 2

a,b = swapper(a=b,b=a)

print(f"{a=}, {b=}")