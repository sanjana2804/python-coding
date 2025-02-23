num=int(input("Enter a number:"))
sum1=0
temp=num
l=len(str(num))
while temp>0:
    digit=temp%10
    sum1+=digit**l
    temp=temp//10

if num==sum1:
    print("armstrong")
else:
    print("not armstrong")
