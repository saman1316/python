numbers=list(range(1,7))
print(numbers)

even_numbers=list(range(2,11,2))
print(even_numbers)

#مربع اعداد کمتر از 10
sequras=[]
for value in range(1,11):
    sequar=value**2
    sequras.append(sequar)
    print(sequar)

sequras=[]
for value in range(1,11):
    sequras.append(value**2)
print(sequras)

sequras=[value**2 for value in  range(1,11)]
print(sequras)



  