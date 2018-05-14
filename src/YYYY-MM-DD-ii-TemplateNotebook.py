
# coding: utf-8

# # Jupyter Notebook Title

# ## Contents of Notebook
# Description of contents
# 

# ### Notebook magic commands

# In[16]:

get_ipython().magic('matplotlib inline')


# ### Notebook imports

# In[17]:

# all imports should go here

import pandas as pd
import sys
import os
import datetime
import platform

import matplotlib.pyplot as plt
import seaborn as sb


# ### Notebook version status

# In[18]:

# show info to support reproducability

print('python version : ' + sys.version)
print('pandas version : ' + pd.__version__)

print('current wkg dir: ' + os.getcwd())
print('Notebook run at: ' + str(datetime.datetime.now())+ ' local time')
print('Notebook run at: ' + str(datetime.datetime.utcnow()) + ' UTC') 
print('Notebook run on: ' + platform.platform())


# ### Customizations for notebook

# In[19]:

# path to saved figures
figure_prefix = '../figures/'


# ### Required notebooks to be run first

# In[20]:

from IPython.display import FileLink
FileLink('../develop/a.ipynb')


# ### Display associated webpages (eg source of data)

# In[25]:

from IPython.display import IFrame
IFrame("http://www.net-analysis.com", width = 800, height = 200)


# ### Save figures to figures directory

# In[24]:

x=[1,2,3,4,5,6]
y=[2,4,5,2,5,9]
nbars = len(x)
plot2 =sb.barplot(x=x, y=y)
plt.savefig(figure_prefix+'TemplateNotebookFigure01.jpg')


# In[ ]:



