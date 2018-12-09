print('Hello, world!')

a = 1
b = 2

def function(z):
    d = 3
    print(a*b*d*z)
    print("z=", z)
    z += 1
    return

c =  int(input("Give integer variable: "))
function(c)
print("c=", c)
