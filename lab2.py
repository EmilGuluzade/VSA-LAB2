n = int(input("Bir reqem girin: "))
c = list(range(n))
print('C:',c)
k=1
for x in c:
    if x%2!=0:
        k*=x
print(k)







