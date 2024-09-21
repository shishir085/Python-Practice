# determine if a fruit is ripe , overripe or unripe based on it color


fruit="banana"
color=input("enter the color of banana: ")

if fruit:
    if color=="green":
        print("Banana is Unripe")
    elif color=="yellow": 
        print("banana is ripe")
    elif color=="brown":
        print("Banana is overripe")
    else:
        print("invalid parameter")    
