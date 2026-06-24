t=(1,2,1.1,2,2.2,10,{100,200,300},20,"tops",False,1,2)

print(t)
print(t.count(1))
print(t.index(10))
for i in t:
    print(i)
t[5].append(400)
print(t)
