import random as np
import numpy as mp
import matplotlib.pyplot as plt
a=np.randint(0,100)
b=np.randint(0,100)
c=np.randint(0,100)
d=np.randint(0,100)
e=np.randint(0,100)
f=np.randint(0,100)
g=np.randint(0,100)
h=np.randint(0,100)
i=np.randint(0,100)
j=np.randint(0,100)
k=np.randint(0,100)
l=np.randint(0,100)
m=np.randint(0,100)
n=np.randint(0,100)
o=np.randint(0,100)
p=np.randint(0,100)
data =[[a,b,c,d,e],[f,g,h,i,j],[l,m,n,o,p]]
t=mp.array([["yash","tapan","saurabh","sanjeet","Ayush"],["yash","tapan","saurabh","sanjeet","Ayush"],["yash","tapan","saurabh","sanjeet","Ayush"]])
plt.xticks([0,1,2,3,4],t[0])
plt.boxplot(data[0],showmeans=True,notch=True,vert=False)
plt.show()
plt.xticks([0,1,2,3,4],t[1])
plt.boxplot(data[1],showmeans=True,notch=True,vert=False)
plt.show()
plt.xticks([0,1,2,3,4],t[2])
plt.boxplot(data[2],showmeans=True,notch=True,vert=False)
plt.show()
