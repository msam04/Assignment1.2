
# coding: utf-8

# In[2]:


first = 0
last = 37
count = 0

for number in (first, last):
    if (number % 7 == 0 and number % 5 != 0):
        count += 1
        if (count == 0):
            print(number)
        else:
            print("," , number)
            
        

