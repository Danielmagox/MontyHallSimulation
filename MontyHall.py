#!/usr/bin/env python
# coding: utf-8

# # Monty Hall problem

# In[11]:


import random


# In[12]:


NUMBER_OF_SIMULATIONS = 1000000
DOORS = [1,0,0]


# In[13]:


def shuffle_doors(doors):
    random.shuffle(doors)
    return doors


# In[14]:


def random_between(minimum=0,maximum=3):
    return random.randrange(minimum,maximum)


# #### Function that chooses the door depending on what is behind it and the player's choice

# In[15]:


def tv_presenter(shuffled_doors,picked_door):
    for i, j in enumerate(shuffled_doors):
        if i == picked_door or j == 1:
            pass
        else:
            shuffled_doors[i] = 2
    return shuffled_doors


# In[16]:


def switch_door(election_doors,picked_door):
    for i,j in enumerate(election_doors):
        if i != picked_door and j != 2:
            return election_doors[i]
        else:
            pass


# In[17]:


def stay_door(election_doors,picked_door):
    return election_doors[picked_door]


# In[18]:


def percentage(hits, total=NUMBER_OF_SIMULATIONS):
    return (hits/total)*100


# #### We can calculate it with the switch funcion or with the stay

# In[19]:


shuffled_doors = []
picked_door = 0
election_doors = []
result = 0
hits = 0
for x in range(NUMBER_OF_SIMULATIONS):
    shuffled_doors = shuffle_doors(DOORS)
    picked_door = random_between()
    election_doors = tv_presenter(shuffled_doors,picked_door)
    result = switch_door(election_doors,picked_door)
    if result == 1:
        hits = hits + 1


# #### As expected, changing doors is much more beneficial than staying, 66% vs 33%.

# In[20]:


percentage(hits,NUMBER_OF_SIMULATIONS)


# In[ ]:




