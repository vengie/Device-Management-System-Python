#!/usr/bin/env python
# coding: utf-8

# In[7]:


import numpy as np
import pandas as pd


# In[8]:


print("\t\t\tWelcome to the Device Management System")

# print(" 1. View all devices \n 2. Add a device \n 3. Delete a device \n 4. Update a device \n 5. Exit the program")


# In[14]:


ch="Y"
while(ch=="Y"):
    n = int(input("Select one option from the list ( 1, 2, 3, 4 or 5 ):"))
    if(n==1):
        f=open("devices.txt","r")
        print(f.read())
        f.close()

    elif(n==2):
        f=open("devices.txt","r+")
        x=f.readlines()
        y=len(x)
        f.close()
        f=open("devices.txt","r")
        f.write("device "+(y+1))
        f.close()
        
    elif(n==3):
        f=open("devices.txt","r")
        x=f.readlines()
        f.close()
        x.pop()
        f=open("devices.txt","w")
        f.writelines(x)
        f.close()
      
    elif(n==4):
        k=input("Enter device code:")
        f=open("devices.txt","a")
        f.write(k)
        f.close()
        
    elif(n==5):
        exit()

    else:
        print("invalid input")
    ch=input("Do you want to continue?(y/n):")
    
#These Function is responsible for print the file 
# def read(d):     
#     for i in d:         
#         print(i,d[i]) #These Function is responsible for add element in the file 

# def add(d):     
#     id1=input("Enter id")     
#     name=input("Enter device name")     
#     d[name]=id1     
#     f = open("devices.txt", "w")     
#     c=0     
#     for i in d:         
#         if c!=0:             
#             s="\n"+i + " " +d[i]              
#             f.write(s)         
#         else:             
#             s=i + " " +d[i]              
#             f.write(s)            
#             c+=1     
#             f.close() #These Function is responsible for update element in the file 
            
# def update(d):     
#     name=input("Enter device name")     
#     id1=input("Enter id")     
#     f = open("devices.txt", "w")     
#     c=0     
#     d[name]=id1     
#     print(d)     
#     for i in d:         
#         if c!=0:             
#             s="\n"+i + " " +d[i]              
#             f.write(s)         
#         else:             
#             s=i + " " +d[i]             
#             f.write(s)             
#             c+=1     
#             f.close() #These Function is responsible for update element in the file 
    
# def delete(d):     
#     d1={}     
#     name=input("Enter device name")     
#     f = open("devices.txt", "w")     
#     c=0     
#     for i in d:         
#         if i!=name:             
#             d1[i]=d[i]     
#     for i in d1:         
#         if c!=0:             
#             s="\n"+i + " " +d1[i]              
#             f.write(s)         
#         else:             
#             s=i + " " +d1[i]              
#             f.write(s)             
#             c+=1                        
#     f.close() 

# while(c<2):     #These below lines is resposible for read the file     
#     f = open("devices.txt", "r")     
#     s=f.read()     
#     f.close()     
#     s=s.split()     
#     d={}     
#     for i in range(len(s)):         
#         if i%2==0:             
#             s1=s[i]             
#             s2=s[i+1]             
#             d[s1]=s2     
#         print("Press 1 for read")     
#         print("Press 2 for add")     
#         print("Press 3 for update")     
#         print("Press 4 for Delete")     
#         print("Press 5 for Exit")     
#         try:         
#             n=int(input("Enter your choice"))     
#         except:         
#             print("Wrong Input")     
#         if(n==1):         
#             read(d)  #call the read function and pass the dictionary which is loaded from file     
#         elif(n==2):         
#             d=add(d) #call the add function and pass the dictionary which is loaded from file     
#         elif(n==3):         
#             update(d) #call the update function and pass the dictionary which is loaded from file     
#         elif(n==4):         
#             delete(d) #call the delete function and pass the dictionary which is loaded from file     
#         elif(n==5):         
#             break;     
#         else:         
#             print("Wrong Input,Plz try Again")     
#         c+=1


# In[ ]:




