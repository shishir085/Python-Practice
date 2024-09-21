# practice 

''' def find_name():
    with open("practice.txt","r") as f:
        data=f.read()

        new_data = data.replace("Java","Python")
        print(new_data)


    with open("practice.txt","w") as f:
        f.write(new_data)

find_name()  '''

# //////////////////////////////////////////

'''with open("practice.txt","r") as f:
    data=f.read()
    if(data.find("learning")):
        print("true")
    else:
        print("false")'''

# /////////////////////////////////////////////

def check_for_line():
    word="learing"
    data=True
    line_no=1
    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if (word in data):
                print(line_no)
                return
            line_no+=1
    return -1

check_for_line()
    
    


    









 
