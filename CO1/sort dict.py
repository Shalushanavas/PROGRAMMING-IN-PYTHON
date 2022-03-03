d={}
n=int(input("Enter the elements"))
for i in range(n):
    key=input("Enter the key: ")
    value=int(input("Enter the value in numeric: "))
    d[key]=value
print(d)

d_rev=sorted(d, key=d.get, reverse=True)
d_nrev=sorted(d,key=d.get)
print("Decending Order",d_rev)
print("Ascending Order",d_nrev)
