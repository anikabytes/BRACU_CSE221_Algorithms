# -*- coding: utf-8 -*-
"""task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1myU9yMehnzXANNwzpxR1iEOAm-V_7LJY
"""

def job_schedule(inp) :

    path = [inp[0]]
    queue = [inp[0]]
    
    ct = 0 
    for i in range(0,len(inp)) :
        if inp[i] not in path :
            if inp[i][0] >= path[ct][1] :
                path.append(inp[i])
                queue.append(inp[i])
                ct += 1 

    return len(path) , path 

def sort(sto) : 
    for i in range(len(sto)-1):
        count = 0  
        for j in range(len(sto)-i-1):
            if int(sto[j][1]) > int(sto[j+1][1]):
                sto[j][1], sto[j+1][1], sto[j][0], sto[j+1][0] = sto[j+1][1], sto[j][1], sto[j+1][0], sto[j][0]
                count += 1
        if count == 0 :
            break 
    return sto 

f = open('/content/task1_input.txt','r')
w = open('/content/task1_output.txt','w')
n = int(f.readline())
lis = []

for i in range(0,n) :
    l = f.readline().split()
    lis.append(l)

count, path = job_schedule(sort(lis))
w.write(f'{count} \n')

for i in path :
    st = ''
    for j in i : 
        st += j + ' '
    w.write(f'{st} \n')

w.close()