# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1A0uYUmm7lw5fUoCtqt3-wE-PAakHR_wP
"""

# Task 3 (i)
def inp(num) :
    lis = []
    l = (f.readline()).split()
    for i in range(0,int(num)) :
        lis.append(int(l[i]))
    n = quickSort(lis,0,len(lis)-1)
    store = ''
    for j in range(0,len(n)) :
        store += str(n[j]) + ' '
    f3 = open('output3(i).txt','w')
    f3.write(store)
        

def quickSort(arr,low,high) :
    if low == high :
        return 
    if low < high :
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)
    return arr 

def partition(arr,low,high) : 

    pivot = arr[high]
    i = low - 1 
    for j in range(low,high) :
        if arr[j] <= pivot :
            i += 1 
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1 


    
f = open('input3(i).txt','r')
f2 = f.readline()
inp(f2)

# Task 3 (ii)
def partition(arr,low,high) : 
    
    if low >= len(arr) :
        low -= 1 
    pivot = arr[high]
    i = low - 1 
    for j in range(low,high) :
        if arr[j] <= pivot :
            i += 1 
            arr[i],arr[j] = arr[j],arr[i]
        if i == -1 :
            break
    arr[i+1],arr[high] = arr[high],arr[i+1]      
    findK(arr,low-1)

def findK(arr,k) :
    for i in range(0,len(arr)) :
        if i == k :
            f2.write(arr[k])


f = open('input3(ii).txt','r')
f2 = open('output3(ii).txt','w')
f1 = f.readlines()
num_lis = ((((f1[0].split('The array: '))[-1]).split('\n'))[0]).split(' ')
k1 = int((f1[1].split('K='))[-1])
k2 = int((f1[2].split('K='))[-1])
k3 = int((f1[3].split('K='))[-1])
k_lis = [k1,k2,k3]
partition(num_lis,k1,len(num_lis)-1)
partition(num_lis,k2,len(num_lis)-1)
partition(num_lis,k3,len(num_lis)-1)