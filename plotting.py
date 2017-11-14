#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:59:11 2017

@author: naveen
"""

import matplotlib.pyplot as plt
import random

f = open("rews_1_2.txt")
content = f.readlines()
f.close()

l = list()

for line in content:
    t = float(line.strip("\n"))
    l.append(t)
    
final = random.sample(l,1000)
plt.plot(final)
plt.show()