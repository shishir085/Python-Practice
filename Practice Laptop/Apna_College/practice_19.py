count=0
with open('practice_19.txt',"r")as f:
    data=f.read()
    
    nums=data.split(',')
    # print(nums)
    for val in nums:
        if (int(val)%2==0):
            count+=1
            # print(val)
        
    print("The number of even numbers in the list is",count)            

