name=['krupa','kruti','nitixa','aesha','shruti']

print(name[2])

name[1]='naliyapara'

print(name)

name.append("kruti")

print(name)

menu=[]

n=int(input("how many items u want to store: "))

for i in range(n):
    items=input("enter item names: ")
    menu.append(items)

print(menu)

a=[23,45,67]
b=a
b.append(21)
print(a)