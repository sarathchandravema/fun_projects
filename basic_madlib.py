#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def madlib():
    adj = input("Adjective:  ")
    verb1 = input("Verb:  ")
    verb2 = input("Verb:  ")
    famous_person = input("Famous person:  ")
    
    madlibs = f"\nComputer Programming is so {adj}! It makes me so excited all the time because I love to {verb1}.     Stay hyderated and {verb2} like you are {famous_person}!"
    
    return madlibs


# In[ ]:


if __name__ == "__main__":
    output = madlib()
    print(output)

