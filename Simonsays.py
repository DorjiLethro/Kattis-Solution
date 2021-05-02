z=int(input())
for i in range(z):
    n=input()
    if n[:10]=="Simon says":
        print(n[11:])
