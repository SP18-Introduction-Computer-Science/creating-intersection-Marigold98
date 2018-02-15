a = [1,4,5,7,8,12]
b = [4,5,9,12,15,2]
def intersectFn(a,b) :
    c = []
    for element in a :
        c.append(element)
    for element in b :
        if element not in c :
            c.append(element)
    return c
output = intersectFn(a,b)

for element in output:
    print(element)
