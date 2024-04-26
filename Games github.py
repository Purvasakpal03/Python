#!/usr/bin/env python
# coding: utf-8

# In[6]:


list_answer = ['apple', 'mango']
list_q = ['ap_le', 'man_o']
point = 0

for i in range(len(list_q)):
    guess = 1
    while guess <= 2:
        user_input = input(f"Fill in the blank for '{list_q[i]}': ")
        if len(user_input) == 1 and user_input == list_answer[i][list_q[i].index('_')]:
            print("Correct!")
            point += 10
            break
        else:
            print("Incorrect answer. Try again.")
            guess += 1
    else:
        print("Incorrect answer. No more chances.")

print("Points:", point)


# In[4]:


series = [2, 4, 6, 8, 10,12]
first_num = series[0]
last_num = series[-1]
full_series = list(range(first_num, last_num + 1))  # Make sure 'list' is not assigned elsewhere as a variable
missing_nums = [num for num in full_series if num not in series]
print("Missing numbers in the series:", missing_nums)


# In[ ]:


string = input("Enter a sentence : ")
vowels = 0
string.lower()

for i in string:
    if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        vowels = vowels + 1 
print("Total Number of Vowels in this String = ", vowels)

