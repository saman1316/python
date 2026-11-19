prompt="\n plese enter the place of born"
prompt+="\n enter 'exit' to end the program:"
while True:
    city=input(prompt)
    if city=="exit":
       break
    else:
        print(f"i was born in {city.title()}")

