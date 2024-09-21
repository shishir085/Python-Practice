# open/close file

f=open("text.txt","r")


# print(f.read())

'''
for  line in open('text.txt'):
    print(line,end="")


with open("text.txt")as g:
    print(g.read())
'''
while True:
    line=f.readline()
    if not line: break
    print(line,end='')