# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wt0P3KYB-hG9Pfgnb7UQh6Fir32f8Qsk
"""

def LCS(X,Y,Z):

    m=len(X)+1
    n=len(Y)+1
    o=len(Z)+1
    
    c=[[[0]*o for i in range(n)] for j in range(m)]
    t=[[[0]*o for i in range(n)] for j in range(m)]

    for i in range(1,m):
        for j in range(1,n):
            for k in range(1,o):
                if X[i-1]==Y[j-1] and X[i-1]==Z[k-1]:

                    c[i][j][k]=1+c[i-1][j-1][k-1]
                    t[i][j][k]='diagonal'

                else:
                    if c[i-1][j][k]>=c[i][j-1][k]:
                        max=c[i-1][j][k]

                        if max>=c[i][j][k-1]:
                            c[i][j][k]=max
                            t[i][j][k]='up-up-left'

                        else:
                            max = c[i][j][k-1]
                            c[i][j][k] =max
                            t[i][j][k]='left-up-up'

                    else:
                        max = c[i][j-1][k]
                        if max >= c[i][j][k-1]:
                            c[i][j][k]=max
                            t[i][j][k]='up-left-up'

                        else:
                            max=c[i][j][k-1]
                            c[i][j][k]=max
                            t[i][j][k]='left-up-up'

    return c[m-1][n-1][o-1]

f = open("/content/input3.txt","r")
f_w = open("/content/output3.txt","w")
X,Y,Z = f.readlines()
X,Y,Z = X.strip(),Y.strip(),Z.strip()
out = LCS(X,Y,Z)
f_w.write(str(out))
f_w.close()