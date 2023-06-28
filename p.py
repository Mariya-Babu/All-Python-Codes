import numpy as np
import math

# Array Declaration's 

# Array Declaration Using Array() 
arr0 = np.array(10)
arr1 = np.array([10,20,30,40,50])
arr2 = np.array([[1,2,3,4,5],[9,8,7,6,11]])
# printing Array Elements 
print(arr0)
print(arr1)
print(arr2[1][3])

# Array Declaration Using asarray()
l1 = [[0,1,2,3,4],[9,8,7,6,5]]
a1 = np.asarray(l1,dtype=int,order='F')
# print(a0)
for i in np.nditer(a1):
    print(i)

# Array Declaration Using frombuffer() 
s = b'Hello World This is Mariya Babu want to become a software engineer'
s0 = np.frombuffer(s,dtype='S1',count=10,offset=6)
print(s0)

# Array Declaration Using fromiter() 
l2 = [11,12,13,14,15]
a2 =  np.fromiter(l2, dtype=float)
print(a2)

# Array Initilaization's 

# Initilaization with zero's 
z = np.zeros([4,5],dtype=int)
print(z)

# Initilaization with one's 
o = np.ones([3,3],dtype=int)
print(o)

# Initilaization with eye(identity Matrix) 
e = np.eye(5,dtype=float)
print(e)

# Initilaization with full() 
f = np.full([6,7],45,dtype=int)
print(f)

# Initilaization with random.rand() 
r = np.random.rand(4,5) * 10
print(r)

# Numerical Ranges 

# Initilaization with arange() 
ar = np.arange(1,34,3,dtype=float)
print(ar)

# Initilaization with linspace() 
lsp = np.linspace(1,34,9, retstep=True)
print(lsp)

# Initilaization with logspace 

log = np.logspace(1, 100)
print(log)

# Array Properties 
rand = np.arange(1,100,10, dtype=float) 
print(rand)
print(np.size(rand))  #size
print(np.shape(rand))  #shape
rand = rand.reshape([5,2])
print(np.shape(rand))
rand = rand.reshape([2,5])
print(np.shape(rand))
print(rand.dtype)  #dtype
rand = rand.reshape(10)
print(np.shape(rand))
# Array Operations 

# Accessing and Slicing 
print(rand[0])
print(rand[5])
print(rand[9])
print(rand[3:])
print(rand[:7])
print(rand[3:8])

# Copy() 
copy = np.copy(rand)
rand[5] = 55
print(copy)
# View()   (view is the referance for the given array)
view = rand.view()
print(view)

#sort()
us = np.array([95, 0, 45, 65, 70, 55, 69, 5, 32, 63])
print(us)
us = np.sort(us)
print(us)

# reshape()
us = us.reshape([2,5])
print(np.shape(us))

# append 
app1 = np.append(arr1,arr2)
print(app1)

arr21 = np.array([[1,2,3,4],[9,8,7,6]])
arr22 = np.array([[10,20,30,40],[90,80,70,60]])
#axis=0 column wise append 
app2 = np.append(arr21,arr22,axis=0) 
print(app2)
#axis=1 row wise append
app3 = np.append(arr21,arr22,axis=1) 
print(app3)

# Concatenate
c1 = np.arange(1,99,7).reshape(2,7)
c2 = np.arange(1,80,6).reshape(2,7)
c3 = np.arange(1,70,5).reshape(2,7)

cr1 = np.concatenate((c1,c2))
print(cr1)
# axis=0 column wise concatenatation 
cr2 = np.concatenate((c1,c2),axis=0)   #vstack
print(cr2)
# axis=1 row wise concatenatation
cr3 = np.concatenate((c1,c2),axis=1)  #hstack
print(cr3)

cr4 = np.concatenate((c1,c2,c3),axis=0)
print(cr4)


# Stack 
sr1 = np.stack((c1,c2))
print(sr1)
# stack with axis=  1
sr2 = np.stack((c1,c2),axis=1)
print(sr2)
# vstack 
sr3 = np.vstack((c1,c2))
print(sr3)
# hstack 
sr4 = np.hstack((c1,c2))
print(sr4)
# dstack 
sr5 = np.dstack((c1,c2))
print(sr5)

