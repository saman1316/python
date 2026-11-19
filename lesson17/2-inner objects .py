users={
    "sam ebrahimi1391":{
        "first name":"sam",
        "last name":"ebrahimi",
        "loction":"akbar abad"
    },
    "mohmad makzani1234":{
        "first name":"mohmad",
        "last name":"makzani",
        "loction":"nasim shar"
    }
}

for username, userinfo in users .items():
    print(f"\n user name :{username}")
    fname=f"{userinfo["first name"]}{userinfo["last name"]}"
    loction= userinfo["loction"]

print(f"\n full name:{fname}")
print(f"\nloction: {loction}")