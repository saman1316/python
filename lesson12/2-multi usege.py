avaible_toppings=["tomato","mushrooms","cheese","olive","corn"]

req_toppings=["tomato","onion","cheese","pine apple"]
for req in req_toppings:
    if req in avaible_toppings:
        print(f"adding: {req}")
    else:
        print(f"sorry we dont have this request{req}")
        print ("\n finished makeinf pizza")
   
