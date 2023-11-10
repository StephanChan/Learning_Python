#!/usr/bin/env python
# coding: utf-8

# In[311]:


print('2*3: ',2*3)
print('2**3: ',2**3)
print('10^1: ',10^1)


# In[14]:


# how to define a list
a=[1,2,3]
print(a)

a=list([1,2,3])
print(a)

a.append(4)
print(a)

a.append([5,6])
print(a)

print(a[0])
print(a[4][1])


# In[60]:


# how to use numpy
import numpy as np
a=np.array([1,2,3])
print(a)

a=np.array(np.arange(0,10))
print(a)

a=np.arange(0,10,0.1)
print(a)

a=np.arange(0,10)
print(a)

print(np.random.random(5))

print(np.random.random())

print('integer random number: ',np.random.randint(0,5))

print(np.random.rand(5))


# In[72]:


# numpy sin functions and number of digits
s=np.sin(30/180*np.pi)
print(s)
print(round(s,2))
print("{:.2f}".format(s))

print(np.arctan(1)/np.pi*180)

s=np.sin(np.arange(0,10,0.5))

for ii in s: 
   print(round(ii,2))


# In[74]:





# In[168]:


# figure properties
x=np.arange(0,np.pi,0.01);
s1=np.sin(10*2*np.pi*x);
s2=np.sin(2*2*np.pi*x);
from matplotlib import pyplot as plt

plt.figure(2)
plt.plot(x,s1)
plt.plot(x,s2)
plt.legend(['s1','s2'],loc='upper right',fontsize=15)
plt.xlim(0,5)
plt.ylim(-1.5,1.5)
plt.title('signal 2',fontsize=20)
plt.xlabel('time',fontsize=15)
plt.ylabel('signal',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)


# In[170]:


# fft
f=np.fft.fft(s1)/len(s1)
f=np.fft.fftshift(f)
plt.figure()
plt.plot(abs(f))
plt.plot(s1)

s2=np.hanning(len(s1))*s1
f=np.fft.fft(s2)/len(s2)
f=np.fft.fftshift(f)
plt.figure()
plt.plot(abs(f))
plt.plot(s2)


# In[172]:


# ifft
s3=np.fft.ifft(np.fft.fftshift(f*len(s2)))
plt.figure()
plt.plot(np.real(s3))
plt.plot(np.imag(s3))
plt.legend(['real','imag'],fontsize=15,loc='upper right')

plt.figure()
f3=np.fft.fftshift(np.fft.fft(s3)/len(s3))
plt.figure
plt.plot(abs(f3))


# In[184]:


# scipy fft is same as numpy fft
from scipy import fft
f=fft.fft(s1)/len(s1)
f=fft.fftshift(f)
plt.figure()
plt.plot(abs(f))
plt.plot(s1)

s2=np.hanning(len(s1))*s1
f=fft.fft(s2)/len(s2)
f=fft.fftshift(f)
plt.figure()
plt.plot(abs(f))
plt.plot(s2)

# ifft
s3=fft.ifft(fft.fftshift(f*len(s2)))
plt.figure()
plt.plot(np.real(s3))
plt.plot(np.imag(s3))
plt.legend(['real','imag'],fontsize=15,loc='upper right')

plt.figure()
f3=fft.fftshift(fft.fft(s3)/len(s3))
plt.figure
plt.plot(abs(f3))


# In[217]:


# least square curve fitting
from scipy.optimize import least_squares as ls

t=np.arange(0,10,0.02)
y=10.3*np.exp(-0.35*t)-np.random.random(len(t))

def model(P,X):
    return P[0]*np.exp(-P[1]*X)+P[2]
def err(P,X,Y):
    return model(P,X)-Y

res = least_squares(err, [1,1,1],  bounds=([0,0,-1],[15,10,10]), args=(t, y))
p=[round(ii,3) for ii in res.x]
print(p)

y0=model(res.x,t)
plt.figure()
plt.plot(t,y0,linewidth=3)
plt.plot(t,y,'o',markersize=2)
plt.title('exponential fitting',fontsize=20)
plt.xlabel('time',fontsize=15)
plt.ylabel('signal',fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)


# In[283]:


m=np.mat(np.array([[1,2],[3,4]]))
m2=np.mat(np.array([[1,2],[2,4]]))

#print(m.T) # transpose
#print(m.I) # inverse
print('m :',m)
print('m shape:',m.shape)
print('m2 :',m2)
print('m*m2 :',m*m2) # if m and m2 are numpy.matrix, this is matrix multiplication,
# else if m and m2 are numpy.array, this will be 点乘
print('np.dot :',np.dot(m,m2))
print('m.dotm2 :',m.dot(m2))
print('np.multiply:',np.multiply(m,m2)) # 点乘


# In[284]:


# eigenvalue decomposition
from scipy import linalg

la, v = linalg.eig(m)
print(la)
print(v[:, 0])
print(v[:, 1])


# In[285]:


# Singular value decomposition
# singular values of a MxN matrix X is the square root of eigenvalues of X^H.dot(X)
U,s,Vh = linalg.svd(m)

print(s)
Sig = np.matrix(linalg.diagsvd(s,m.shape[0],m.shape[1]))
print(U.dot(Sig.dot(Vh)))


# In[299]:


# exponential of matrix e^Matrix
print(linalg.expm(m))

print('exponential of matrix element')
e_m=[[np.exp(ii) for ii in jj] for jj in np.array(m)] # exponential of matrix element
print(np.matrix(e_m))


# In[323]:


# log of matrix
print(linalg.logm(m))

print('log of matrix element')
e_m=[[np.log(ii) for ii in jj] for jj in np.array(m)] # exponential of matrix element
print(np.matrix(e_m))


# In[320]:


# square of elements
m_2=[[ii**3 for ii in kk] for kk in np.array(m)]
print(np.matrix(m_2))
print('np.array(m)**3')
print(np.array(m)**3)
print('m**3')
print(m**3)
print('m.dot(m.dot(m))')
print(m.dot(m.dot(m)))


# In[ ]:





# In[ ]:





# In[ ]:




