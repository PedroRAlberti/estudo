a = "abacate"
b = "acabate"
def fun(a,b):
    list_a = []
    list_b = []
    for i in a:
        list_a.append(ord(i))
    for i in b:
        list_b.append(ord(i))
    list1 = sorted(list_a)
    list2 = sorted(list_b)
    if list1 == list2:
        return True
    else:
        return False
print(fun(a,b))