def fun(a):
    frase = ""
    for i in a:
        if i == "a":
            frase += 'z'
        else:
            c = ord(i)
            if c > 97 and c < 123:
                frase += chr(c - 1)
            else:
                frase += chr(c)
    print(frase)
a = "abz{"
fun(a)