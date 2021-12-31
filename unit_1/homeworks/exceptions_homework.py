
try:
    a = 12
    s = "hello"
    print(a+s)
except TypeError:
    if(type(a)==int):
        a=str(a)
    else:
        s=str(s)
    print(a+s)
    