# string

str="Shishir_Pandey"
# print(len(str))
# print(str[4])

#slice in python
"""
str1="Crimson_College"
print(str1 [0:7])   # it denotes that slice will occur from the first index to 7th index of the string
print(str1 [:7])   # it denotes that slice will occur from the first index to 7th index of the string
print(str1 [0:])   # it denotes that slice will occur from the index to last index of the string
print(str1 [8:len(str1)])    #from 8 index to last index . len  denotes moving to the last of the string

"""
# string functions


text="i am a coder from crimson college"

text1=text.endswith("ge")#checks if the string ends with the word we are searching for
print(text1)
     
print(text.capitalize())     #capitalizes the first letter of the string
print(text,"\n")


print(text.replace("a","e")) #replaces the word with the word we are replacing

print(text.find("from"))  #finds the first index of the word we are searching for

print(text.count("e"))




