temp=25
is_raining=False
if temp>35 or temp<0 or is_raining:
    print("the outdoor event is cancled.")
else:
    print("we can go outside no issues")


#ternary opeartor
num=5
a,b=6,7
print("positive" if num >0 else "negitive")
print("even" if num%2==0 else "ODD")
max=a if a>b else b
print(max)
