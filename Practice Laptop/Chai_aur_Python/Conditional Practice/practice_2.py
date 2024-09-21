user_age=int(input("enter you age for movie tickets: "))
movie_day=input("enter the day of movie watching: ")


price=12 if user_age>=18 else 8



if movie_day=='wednesday':
    price-=2

print("Ticket price for you is ",price,"$")
'''
if user_age>=18:
    print("price of ticket is 12$")
    
elif user_age<18:
    print("price of ticket is 8$")
'''
