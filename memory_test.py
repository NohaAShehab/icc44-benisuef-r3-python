list2=[]
list1 = []
number = input("please enter number : ")
if number.isdigit():
    number = int(number)
    for x in range(1 , number+1):
        list1 = []
        for y in range(1, x+1):
            list1.append(x*y)
        list2.append(list1)
    print(list2)
else:
    print("--- please enter valid number ")