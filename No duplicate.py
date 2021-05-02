n=input()
p=n.split()
count=[]
total=0
for i in range(len(p)):
    if p[i] not in count:
        count.append(p[i])
        total+=1
if len(p)==total:
    print("yes")
else:
    print("no")
