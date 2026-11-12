age=64

if age < 4: 
   # print("your admission is free")
elif age < 18:
    print("your admisson is 25$")
else:
    #print("your admission is 65$")
#روش دوم
if age< 4:
    price="free"
elif age< 18:
    price=25
elif age<65:
    price=100
elif age>=65:
    price =25
    print (f"your admisson cost in{price}")


