from vpython import *
import numpy as np
N = 100
R, lamda = 1.0, 500E-9
d = 100E-6
dx, dy = d/N, d/N
scene1 = canvas(align = 'left', height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene2 = canvas(align = 'right', x=600, height=600, width=600, center = vector(N*dx/2, N*dy/2, 0))
scene1.lights, scene2.lights = [], []
scene1.ambient, scene2.ambient = color.gray(0.99), color.gray(0.99)
side = np.linspace(-0.01*pi, 0.01*pi, N)
x,y = np.meshgrid(side,side)
E_field = np.zeros((N,N))

k = 2*pi/lamda

for iterX in range(N):
    for iterY in range(N):
        if((iterX - 0.5*N)**2 + (iterY - 0.5*N)**2) <= (0.5*N)**2:
            E_field += (np.cos( k*x*(iterX*dx - d/2)/R + k*y*(iterY*dy - d/2)/R)/R)
Inte = np.abs(E_field)**2
maxI = np.amax(Inte)
for i in range(N):
    for j in range(N):
        box(canvas = scene1, pos=vector(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
            color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))
index = int(N/2)
min = Inte[index][int(N/2)]

while True:
    if Inte[index][int(N/2)] <= min:
        min = Inte[index][int(N/2)]
        index += 1
    else:
        print("simulated Rayleigh criterion",(0.02*pi/N)*(index-N/2))
        break
Inte = np.abs(E_field)
maxI = np.amax(Inte)
for i in range (N):
    for j in range (N):
        box(canvas = scene2,pos = vector(i*dx,j*dy,0),length = dx,height = dy,width =dx,color=vector(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))
print("Theory Rayleigh criterion",1.22*lamda/d)