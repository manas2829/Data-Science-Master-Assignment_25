#!/usr/bin/env python
# coding: utf-8

# # Assigment _ 26-02-2023

# ## Consider the below code to answer further questions:
# 
# ### import numpy as np
# ### List_ = [ '1','2','3','4','5']
# ### array_list = np.array (object = list_)
# 
# ### Ans:-

# In[1]:


import numpy as np


# In[2]:


list_= (['1','2','3','4','5'])
array_list = np.array(['1','2','3','4','5'])
array_list


# In[ ]:





# ## 1. Is there any difference in the data type of variable list_ and array_list?if there is then write a code to print the types of both the variable.
# 
# ### Ans:-
# 
#        In Python, a list is a built-in data structure that can hold a collection of items of different types. On the other 
#        hand, an array is a data structure that can hold a collection of items of the same data type. In Python, the array 
#        module provides support for creating arrays. However, NumPy is a popular Python library that provides a powerful 
#        ndarray (N-dimensional array) object that is widely used for scientific computing and data analysis.
#        
#        

# In[3]:


list_= (['1','2','3','4','5'])
array_list = np.array(list_)
print(type(list))
print(type(array_list))


# ### 
#         As you can see, the type of list_ is list, while the type of array_list is numpy.ndarray. This indicates that they z
#         are different data types.

# ## 2. Write a code to print the data type of each and every element of both the veriables list_ and array_list.
# 
# ### Ans:-

# In[4]:


arr = [1,'Manas',3.14,True]
array_list =np.array(arr)


# In[5]:


for item in arr:
    print(type(item))


# In[6]:


for item in array_list:
    print(type(array_list))


# ## 3. Considering the following changes in the variable, array_list:
# ### array_list = np.array(object = list_, dtype = int)
# ### will there be any difference in the data type of the elements present in both the variables list_ and array_list ? if so print the data types of each and every element present in both the variables, list and array_list. 
# 
# ### Ans:-

# In[7]:


import numpy as np


# In[8]:


list_= (['1',2,'3','4',True])
array_list = np.array(object=list_,dtype=int)


# In[9]:


for item in list_:
    print(type(item))


# In[10]:


for item in array_list:
    print(type(array_list))


# In[11]:


num_list = [[1,2,3],[4,5,6]]
num_arry = np.array(num_list)


# ## 4. write a code to find the following characteristics of variable, num_array:
# ### (i) shape
# ### (ii) size
# 
# ### Ans:-

# In[20]:


num_list = [[1,2,3],[4,5,6]]
num_arry = np.array(num_list)
print(num_arry.size)


# In[22]:


num_list = [[1,2,3],[4,5,6]]
num_arry = np.array(num_list)
print(num_arry.shape)


# ## 5. Write a code to create numpy array of 3*3 matrix containing zeros only, using a numpy array creation function.
# ### [Hint : The size of the array will be 9 and the shape will be (3,3).]
# 
# ### Ans:-

# In[23]:


import numpy as np
arr=np.zeros((3,3))
print(arr)


# In[24]:


arr.size


# In[25]:


arr.shape


# ## 6. Create an identity matrix of shape (5,5)using numpy function?
# 
# ### [Hint : An identity matrix is a matrix containing 1 digonally and other elements will be 0.]
# 
# ### Ans:-

# In[26]:


matrix = np.eye(5)
print(matrix)


# In[27]:


matrix.size


# In[28]:


matrix.shape

