import numpy as np
from matplotlib import pyplot as plt

N=11
x=np.linspace(0,1,N)
dx=1/(N-1)

M=7
T=2
t=np.linspace(0,T,M)
dt=1/(M-1)

lbda=dt/(dx**2)

def Mat(N):
    d=np.ones(N)*(1+2*lbda)
    d1=np.ones(N-1)*(-lbda)
    M=np.diag(d)+np.diag(d1,1)+np.diag(d1,-1)
    return M

A=Mat(N)

def f(x):
    return x*(1-x)

U=[]
for i in range(len(x)):
    U.append(f(x[i]))
plt.plot(x,U)
plt.show()

def norm_inf(u):
    return abs(max(u))

N=[norm_inf(U)]
for j in range(1,len(t)):
    title="U"+str(j)
    U=np.dot(np.linalg.inv(A),U)
    #U[-1]=0
    #U[0]=1
    plt.plot(x,U)
    plt.title(title)
    plt.show()
    
    Ninf=norm_inf(U)
    N.append(Ninf)

Ninf=norm_inf(U)

plt.plot(t,N)
plt.title("Norme inf")
plt.xlabel("t")
plt.show()