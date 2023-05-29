#!/usr/bin/env python
# coding: utf-8

# # Variables in Python

# In[1]:


x = 22

print(x)


# In[2]:


type(x)


# In[1]:


y = 'Mint Chocolate chip'

print(y)


# In[2]:


type (y)


# 
# # Overrides
# 

# In[3]:


y = 'Chocolate'

y = 'Mint Chocolate chip'

print(y)


# In[5]:


Y = 'Chocolate'

y = 'Mint Chocolate chip'

print(Y)


# 
# 
# 
# 
# 
# # Assign multiple values to multiple variables:
# 

# In[6]:


x,y,z = 'Chocolate', 'Vanilla', 'Rocky Road'

print(x)
print(y)
print(z)


# 
# 
# 
# 
# 
# # Assign multiple variables to one value:
# 
# 

# In[7]:


x = y = z = 'Root beer Float'

print(x)
print(y)
print(z)


# In[ ]:





# 
# 
# # Creating a List variable
# 

# In[8]:


ice_cream = ['Chocolate', 'Vanilla', 'Rocky Road']

x,y,z = ice_cream

print(x)
print(y)
print(z)


# In[ ]:





# 
# 
# 
# 
# # Naming Variables (Best Practices)
# 

# In[ ]:


#Camel Case

#Test Variable Case

testVariableCase = 'Vanilla Swirl'


# In[ ]:


#Pascal Case

#Test Variable Case

TestVariableCase = 'Vanilla Swirl'


# In[ ]:


#Snake Case

#Test Variable Case

test_variable_case = 'Vanilla Swirl'


# 
# 
# ### DO THIS

# In[ ]:


testvar = 'Vanilla Swirl'
test_var = 'Vanilla Swirl'
_test_var = 'Vanilla Swirl'
testVar = 'Vanilla Swirl'
TestVar = 'Vanilla Swirl'
testVar2 = 'Vanilla Swirl'


# In[ ]:





# 
# 
# ### DON'T DO THIS

# In[ ]:


2testVar = 'Vanilla Swirl'
test-Var2 = 'Vanilla Swirl'
test Var2 = 'Vanilla Swirl'
test,Var2 = 'Vanilla Swirl'


# In[ ]:





# 
# 
# 
# # Operators with Variables
# 

# In[12]:


## String + String

x = 'Ice Cream is my favorite' + '!!!'

print (x)


# In[14]:


## Integer + Integer

x = 3 + 2

print (x)


# In[11]:


## We cannot add a String and Integer

x = 'Ice Cream is my favorite' + 2

print (x)


# In[ ]:





# In[3]:


x = 'Ice Cream'
y = ' is'
z = ' my favorite'

print (x+y+z)


# In[4]:


x = 1
y = 2
z = 3

print (x+y+z)


# In[ ]:





# In[5]:


## Combine a String and Integer using a COMMA


x = 'Ice Cream'
y = 2


print (x,y)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




