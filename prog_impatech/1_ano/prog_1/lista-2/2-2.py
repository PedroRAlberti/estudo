a = [7,3,4,2,11,15]
b = 9
def target(a,b):
    for i in a:
        for j in a:
            if i + j == b:
                print (a.index(i),a.index(j))
target(a,b)