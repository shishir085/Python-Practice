

given_num=int(input('enter a number: '))
even_sum=0
for i in range(1,given_num+1):
    if i%2==0:
        even_sum+=1
print("sum of even is :", even_sum)
