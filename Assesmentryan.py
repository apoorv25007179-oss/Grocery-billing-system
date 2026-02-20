a=float(input())
b=float(input())
c=float(input())
total=a+b+c
if total>50:
    discount=total*0.10
else:
    discount=0
final=total-discount
print("Original Total:",total)
print("Discount:",discount)
print("Final Amount:",final)
