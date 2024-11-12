b = [.5,.25,.5,.25,1.5,0]
def average(a):
    sum = 0
    num = len(a)
    for i in a:
        sum +=i
    print (sum/num)
average(b)