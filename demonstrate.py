#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Addorder

print('————————————————————————')
print('Addorder函数库演示1.00')
print('————————————————————————')
print('')
print('函数库包含函数:')
print('Addorder.trans()  作用：把str类型的变量指令转换为int返回值 ')
print('Addorder.transinput()  作用：把键盘输入的指令转换为int返回值 ')
print('')
print('指令：transinput 执行Addorder.transinput()函数并输出返回值 ')
print('')

n=0
while n==0:
    
    a=Addorder.transinput()
    if a == 34576631987198:
        print('请输入打算转换为int值的指令:')
        b=Addorder.transinput()
        print(b)
        
    print('')


# In[ ]:




