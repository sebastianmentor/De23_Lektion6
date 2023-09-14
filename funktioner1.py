x = 10
y = 9
z = 8

def f():
    x = 1
    y = 2 
    z = 3 
    var = 4
    print(x,y,z,var)
    return var

for i in range(5):
    var = i
print(f())
print(var)