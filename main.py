logs = []

def sum(a, b):
    logs.append('sum')
    if isinstance(a, str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a+b

def substr(a, b):
    logs.append('substarction')
    if isinstance(a, str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a-b

def mult(a, b):
    logs.append('multiplication')
    if isinstance(a, str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a*b

def divis(a, b):
    try:
        logs.append('division')
        if isinstance(a, str) or isinstance(b,str):
            print("vale andmed")
            return ""
        return a/b
    except ZeroDivisionError:
        print("ei saa jagada nullile")
        return ""

def showLogs(logs):
    summ = 0
    sub = 0
    mult = 0
    div = 0
    for elem in logs:
        if elem == "sum":
            summ  += 1
        elif elem == "substarction":
            sub += 1
        elif elem == "multiplication":
            mult += 1
        else:
            div +=1
    return [summ,sub,mult,div]

print(sum(5, 5))
print(substr(5, 5))
print(mult(5, 5))
print(divis(5, 0))
print(showLogs(logs))
