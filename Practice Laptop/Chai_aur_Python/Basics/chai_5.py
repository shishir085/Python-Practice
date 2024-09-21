# lists

chai_list=['Black','Green','Oolong','White']
print(chai_list[0:5:2])

# chai_list[2]="Herbal"
# print(chai_list)

chai_list[2:3]=["Masala"]
print(chai_list)

chai_list[1:3]="lemon",'coffee'
print(chai_list)

chai_list1=['Black','Green','Oolong','White']

chai_list1[1:1]="test",'test'
print(chai_list1)

chai_list1[1:3]=[]
print(chai_list1)


for tea in chai_list:
    print(tea)