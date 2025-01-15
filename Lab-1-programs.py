#!/usr/bin/env python
# coding: utf-8

# In[41]:


#1. WAP to print biodata using python, dictionary
biodata= {"name": "Sneha Saha", "roll": 22054377, "degree": "BTech", "course": "CSE", "grad": 2026}
print("Student biodata:\n")
print(biodata["name"])
print(biodata["roll"])
print(biodata["degree"])
print(biodata["course"])
print(biodata["grad"])


# In[15]:


#2. Two elements swapping in a list

num= [12, 34, 44, 2, 34, 89, 0]
print("list before swap: ", num)
temp= num[0]
num[0]= num[4]
num[4]= temp
print("list after swap: ", num)


# In[19]:


#3. Ways to check if an element exists in a list
num2= [79, 66, "tau", "pi", 90, 97, 44, 3.2333]
if "tau" in num2:
    print("\'tau\' present in list")
else:
    print("not present")


# In[25]:


#4. Find smallest and largest in a list
a = [8, 3, 5, 1, 9, 12, 233, 12.09, 0.66, 34, 6]
smallest= a[0]
largest= a[0]

for x in a:
    if x < smallest:
        smallest= x
    if x > largest:
        largest= x
print("Smallest and largest elements respectively:")
print(smallest, "\t", largest)


# In[35]:


#5. Print all even numbers in a tuple

b= (12.3, 45.22, 3, 78, 9, 33, 21, 44, 12)
for y in b:
    if(y%2)==0:
        print(y)


# In[37]:


#6. Print positive numbers of a tuple
b= (12.3, -45.22, -3, 78, 9, 33, -21, 44, 12)
for y in b:
    if y>=0:
        print(y)


# In[ ]:




