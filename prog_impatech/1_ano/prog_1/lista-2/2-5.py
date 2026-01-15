a = [.5,.25,.5,.25,1.5,0]
def average(a): 
    sum = 0
    num = len(a)
    for i in a:
        sum +=i
    return (sum/num)
def minus_num(a,b):
    y =[]
    for i in a:
        y.append(i-b)
    return y                                                                                                                                                            -
def std_deviation(a):
    z = []
    y = 0
    x = 0
    z = minus_num(a,average(a))
    for i in z:
        y += (i**2)/(len(a))
    print(y**(1/2))
std_deviation(a)