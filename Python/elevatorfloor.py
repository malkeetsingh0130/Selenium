inp=input("Which country are you in? ").lower()
floor=int(input("Which floor are you on? "))
print(type(inp))
if inp!="us":
    usfloor=floor+1
    print("us floor",usfloor)
else:
    print("US floor",floor)