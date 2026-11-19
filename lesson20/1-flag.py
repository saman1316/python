prompt="\n tell me somethings,and i will reapet it back to you"
prompt+="\n enter 'exit' to end the program:???"

active=True

while active :
    mesasage=input (prompt)
    if mesasage=="exit":
        active=False
    else:
        print(mesasage)



