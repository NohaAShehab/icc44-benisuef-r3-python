list2=[]
# list1 = []
# number = input("please enter number : ")
# if number.isdigit():
#     number = int(number)
#     for x in range(1 , number+1):
#         list1 = []
#         for y in range(1, x+1):
#             list1.append(x*y)
#         list2.append(list1)
#     print(list2)
# else:
# #     print("--- please enter valid number ")
# myl= ''
# print(myl)
#
# l =[ ]
# l.append('')


#####################3 functions
def askforname():
    username  = input("Enter your name: ")
    if username.isalpha():
        print(f'name= {username}')
    else:
        print("--not valid name ")


askforname()
print("----test")


temp = 'My name is {anyname}, I works at {anywork}'
print(temp.format(anyname='', anywork=''))


temp2= 'course= {coursename}'
print(temp2.format(coursename="abc"))






