#!/usr/bin/env python
# coding: utf-8

# In[14]:


1 + 1000


# In[15]:


import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin((5 * 2)* np.pi * t)

# Note that using plt.subplots below is equivalent to using
# fig = plt.figure() and then ax = fig.add_subplot(111)
fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)', title='Sine Wave')
ax.grid()


# In[16]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
img=mpimg.imread('../bentley-bears.jpeg')
plt.imshow(img)
plt.axis('off')
plt.colorbar()


# In[ ]:




