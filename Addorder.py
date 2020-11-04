#!/usr/bin/env python
# coding: utf-8

# In[1]:


def transinput():
    '''把指令转换为一个int值'''
    input1=input() ##输入指令
    i=len(input1)
    n1 = 0
    n2 = 1
    a = ''
    while i>0 :  ##指令转换为数字字符串代码
        a1 = input1[n1:n2] ##顺序读取字符串
        a1 = ord(a1) ##把读取的字符串转换为ASCII码
        a1 = str(a1)
        a += a1
        i-=1
        n1+=1
        n2+=1


    i = len(a)
    n1 = 0
    n2 = 1
    b = '1'
    while i>0 :##数字字符串代码转换为二进制代码
        b1 = a[n1:n2]
        b1 = int(b1)
        if b1==0:
            b1=''
        elif b1==1:
            b1='1'
        elif b1==2:
            b1='10'
        elif b1==3:
            b1='11'
        elif b1==4:
            b1='100'
        elif b1==5:
            b1='101'
        elif b1==6:
            b1='110'
        elif b1==7:
            b1='111'
        elif b1==8:
            b1='1000'
        elif b1==9:
            b1='1001'
        b += b1
        i-=1
        n1+=1
        n2+=1

    sha= int(b,2)
    return sha


# In[5]:


def trans(x):
    '''把x指令转换为一个int值，x得为str类型'''
    i=len(x)
    n1 = 0
    n2 = 1
    a = ''
    while i>0 :  ##指令转换为数字字符串代码
        a1 = x[n1:n2] ##顺序读取字符串
        a1 = ord(a1) ##把读取的字符串转换为ASCII码
        a1 = str(a1)
        a += a1
        i-=1
        n1+=1
        n2+=1


    i = len(a)
    n1 = 0
    n2 = 1
    b = '1'
    while i>0 :##数字字符串代码转换为二进制代码
        b1 = a[n1:n2]
        b1 = int(b1)
        if b1==0:
            b1=''
        elif b1==1:
            b1='1'
        elif b1==2:
            b1='10'
        elif b1==3:
            b1='11'
        elif b1==4:
            b1='100'
        elif b1==5:
            b1='101'
        elif b1==6:
            b1='110'
        elif b1==7:
            b1='111'
        elif b1==8:
            b1='1000'
        elif b1==9:
            b1='1001'
        b += b1
        i-=1
        n1+=1
        n2+=1

    sha= int(b,2)
    return sha


# In[ ]:




