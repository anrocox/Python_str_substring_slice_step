#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 15, 2014

@author: anroco

How to get substrings using the parameter step of slices notation in python?

¿Como obtener substrings usando el parametro step de la notacion slices en
python?
'''

#create a str
s = '-h-e-l-l-o- -w-o-r-l-d-'
print(s)

#s[start:stop:step]
#step specify an increment between the characters to cut of the string.
s_new = s[1:10:2]
print(s_new)

#when step is negative the jump is made back
s_new = s[-2:-11:-2]
print(s_new)

#returns a copy of s with a jump every 4 characters.
s_new = s[1:-1:4]
print(s_new)

#returns a copy of s with a jump every 2 characters.
s_new = s[1:-1:2]
print(s_new)
