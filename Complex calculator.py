#!/usr/bin/env python
# coding: utf-8

# In[8]:


num_1  = int(input("Enter your First Number : "))
Operation = str(input("Enter your Operation(In SYMBOLS): "))
num_2  = int(input("Enter your Second Number : "))
if Operation =="+":
    result = num_1 + num_2
    print("The Sum of the numbers is: ",result)
elif Operation =="-":
    print("Do you want the result in negative form (yes/no) ?")
    userans = str(input("Type yes or no: "))
    if userans =="yes" or userans =="Yes":
        if num_1 > num_2:
            result = num_2 - num_1
            print("Your result is",result)
        elif num_1 < num_2:
            result = num_1 - num_2
            print("Your result is :",result)
    if userans =="no" or userans =="No":
        if num_1 > num_2:
            result = num_1  - num_2
            print("The result is :",result)
        elif num_1 < num_2:
            result = num_2 - num_1
            print("The result is :",result)
elif Operation =="*":
    result = num_1 * num_2
    print("The result of their multiplication is :",result)
elif Operation =="/":
    print("Which number should be the numerator ?")
    userans2 = int(input("Type the number which should be the numerator : "))
    if userans2 == num_1:
        result = (num_1 / num_2)
        print("The result is :" , result)
    elif userans2 == num_2:
        result = (num_2 / num_1)
        print("The result is :" , result)
    else:
        print("ERROR")
        print("TYPED INVALID NUMBER.")


# In[ ]:




