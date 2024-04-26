#!/usr/bin/env python
# coding: utf-8

# In[2]:


dic={"id":101,"Name":"Raman","Salary":10000,"Designation":"Developer","id":10,"Name":"Kiran"}
print(dic["id"])
print(dic["Name"])
print(dic["Salary"])
print(dic["Designation"])
print("id: ",dic.get("id"))
print("Name: ",dic.get("Name"))


# In[3]:


dict2 = {'age' : 22}
dict1.update(dict2)
print(dict1)


# In[4]:


c1 = {'id' : 1, 'name' : 'Rahul', 'designation' : 'CEO'}
c2 = {'id' : 2, 'name' : 'Kartik', 'designation' : 'CEO'}
pd = {'child1':c1, 'child2':c2}
# print(pd)
for i, j in pd.items():
    print('key',i)
    print('value',j)


# In[ ]:





# In[5]:


list1=[(1,2,3), (2,5,6),(4,8,22),(7,1,5)]

# second=list1[-2]
# for i in list1:

#     sort(tuples)
#     print(tuples,key=second)
# print(sort(list1))

for i in list1:
    print(sorted((i[1])))
# def last(n):
#     return n[-2]  
  
# def sort(tuples):
#     return sorted(tuples, key=last)
  
# list1=[(1,2,3), (2,5,6),(2,8,22),(7,1,5)]
# print("Sorted:")
# print(sort(list1))


# In[3]:


student={}
student[1]=101
student[2]=102
print(student)

# sports={"name":"cricketers","players":13,"gametype":"outdoor","dresscode":"white"}
# sports.update({"salary":100000})#TO ADD A NEW ITEM IN THE DICTIONARY
# sports.pop("name")#REMOVES THE DEFINED KEY AND  VALUE
# sports.popitem() #REMOVES THE LAST INSERTED KEY AND VALUE
# sports.clear()#REMOVES ALL  THE ITEMS FROM THE DICTIONARY
# print(sports)

# dic={"id":101,"Name":"Raman","Salary":10000,"Designation":"Developer","id":10,"Name":"Kiran"}
# print(dic["id"])
# print(dic["Name"])
# print(dic["Salary"])
# print(dic["Designation"])
# print("id: ",dic.get("id"))
# print("Name: ",dic.get("Name"))


# In[9]:


student={}
student[1]="Kiran"
student[2]="Gourab"
student[3]="Harry"
print(student)


# In[7]:


dic={"id":101,"Name":"Rahul","Salary":18000,"Designation":"Sales Person"}
for i in dic.items():
    print(i)


# In[4]:


for i,j in dic.items():
    print(i,j)



# In[5]:


dic={"id" : 101, "name": "raman", "Salaey" : 10000, "Designation" : "Developer" }
print(dic["id"])


# In[6]:


for i in dic.items():
    print(i)


# In[10]:


emp={"id" : 101, "name": "raman", "Salary" : 10000}
print("items",emp.items())
print("keys",emp.keys())
print("values",emp.values())


# In[12]:


# HOW TO CREATE A LIST INSIDE A DICTIONARY
student={"id": 101,"name": "Raman","Fees":50000,"Courses":["Java","Python","C++","C","Python"]}
print(student)



# In[13]:


#HOW TO CREATE A DICTIONARY INSIDE A LIST
Employees=[{"id" :101,"name":"Rahul","Salary":18000},
           {"id" :102,"name":"Kiran","Salary":22000},
            {"id" :103,"name":"Radhika","Salary":32700}]
print(Employees[1])


# In[22]:


sports={"name":"cricketers","players":13,"gametype":"outdoor","dresscode":"white"}
sports.update({"salary":100000})#TO ADD A NEW ITEM IN THE DICTIONARY
sports.pop("name")#REMOVES THE DEFINED KEY AND  VALUE
sports.popitem() #REMOVES THE LAST INSERTED KEY AND VALUE
sports.clear()#REMOVES ALL  THE ITEMS FROM THE DICTIONARY
print(sports)



# In[16]:


dic={"id":101,"Name":"Raman","Salary":10000,"Designation":"Developer","id":10,"Name":"Kiran"}
print(dic["id"])
print(dic["Name"])
print(dic["Salary"])
print(dic["Designation"])
print("id: ",dic.get("id"))
print("Name: ",dic.get("Name"))

