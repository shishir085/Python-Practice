# find the first non repeating character

string=input("enter a string: ")
non_repeat=''
for char in string:
    repeat_char=string.count(char)
    if repeat_char==1:
        print("non repeated character is: ",char)
        break
   
        

