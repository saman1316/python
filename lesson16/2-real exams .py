aliens =[]

for alien in range(30):
    new_alien={
        "color":"green",
        "point":5,
        "speed":"slow"
    }
    aliens.append(new_alien)
    for alien_item in aliens[:5]:
        print( alien_item)
    print("....")
    print(f"total number of alien'is{len(aliens)}")