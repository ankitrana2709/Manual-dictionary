aa = ['app', 'vasu']

for a in aa:
    print(a)

def capit(lis):
    new = []
    for a in lis:
        a=a.capitalize()
        new.append(a)
    lis = new
    return(lis)

print(capit(aa))
