z=int(input("Let us know your age; "))

kid = 15
young = 30
adult = 50

if z!=0 and z<=kid:
    print("You're just a kid! XD")
elif z>kid and z<=adult:
    print("You're still young :)")
elif z>=young and not z>=adult:
    print("You're an adult)) ")
elif z>adult:
    print("You're old :X")
else:
    print("Give us a proper number!")


