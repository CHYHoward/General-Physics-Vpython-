from vpython import *
from diatomic import *
N = 20 # 20 molecules
L = ((24.4E-3/(6E23))*N)**(1/3.0)/50 # 2L is the length of the cubic container box, the number is made up
m = 14E-3/6E23 # average mass of O and C
k, T = 1.38E-23, 298.0 # some constants to set up the initial speed
initial_v = (3*k*T/m)**0.5 # some constant
scene = canvas(width = 400, height =400, align = 'left', background = vec(1, 1, 1))
container = box(length = 2*L, height = 2*L, width = 2*L, opacity=0.4, color = color.yellow )
energies = graph(width = 600, align = 'left', ymin=0)
c_avg_com_K = gcurve(color = color.green)
c_avg_v_P = gcurve(color = color.red)
c_avg_v_K = gcurve(color = color.purple)
c_avg_r_K = gcurve(color = color.blue)
COs=[]
for i in range(N): # initialize the 20 CO molecules
    O_pos = vec(random()-0.5, random()-0.5, random()-0.5)*L # random() yields a random number between 0 and 1
    CO = CO_molecule(pos=O_pos, axis = vector(1.0*d, 0, 0)) # generate one CO molecule
    CO.C.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) # set up the initial velocity of C randomly
    CO.O.v = vector(initial_v*random(), initial_v*random(), initial_v*random()) # set up the initial velocity of O randomly
    COs.append(CO) # store this molecule into list COs
times = 0 # number of loops that has been run

totalcomk = 0.0
totalvk = 0.0
totalvp = 0.0
totalrk = 0.0

dt = 5E-16
t = 0
while True:
    rate(3000)
    
    for CO in COs:
        CO.time_lapse(dt)
    for i in range(N-1): # the first N-1 molecules
        for j in range(i+1,N):
            
            if mag(COs[i].C.pos-COs[j].O.pos)<=2*size and dot(COs[i].C.pos-COs[j].O.pos,COs[i].C.v-COs[j].O.v)<=0: 
                (COs[i].C.v,COs[j].O.v) = collision(COs[i].C,COs[j].O)
            if mag(COs[i].C.pos-COs[j].C.pos)<=2*size and dot(COs[i].C.pos-COs[j].C.pos,COs[i].C.v-COs[j].C.v)<=0: 
                (COs[i].C.v,COs[j].C.v) = collision(COs[i].C,COs[j].C)
            if mag(COs[i].O.pos-COs[j].O.pos)<=2*size and dot(COs[i].O.pos-COs[j].O.pos,COs[i].O.v-COs[j].O.v)<=0: 
                (COs[i].O.v,COs[j].O.v) = collision(COs[i].O,COs[j].O)
            if mag(COs[i].O.pos-COs[j].C.pos)<=2*size and dot(COs[i].O.pos-COs[j].C.pos,COs[i].O.v-COs[j].C.v)<=0: 
                (COs[i].O.v,COs[j].C.v) = collision(COs[i].O,COs[j].C)
        
    for CO in COs:
        
        if(CO.C.pos.x<=-L+size and CO.C.v.x<=0) or (CO.C.pos.x>=L-size and CO.C.v.x>=0):
            CO.C.v.x = -CO.C.v.x
        if(CO.C.pos.y<=-L+size and CO.C.v.y<=0) or (CO.C.pos.y>=L-size and CO.C.v.y>=0):
            CO.C.v.y = -CO.C.v.y
        if(CO.C.pos.z<=-L+size and CO.C.v.z<=0) or (CO.C.pos.z>=L-size and CO.C.v.z>=0):
            CO.C.v.z = -CO.C.v.z
        if(CO.O.pos.x<=-L+size and CO.O.v.x<=0) or (CO.O.pos.x>=L-size and CO.O.v.x>=0):
            CO.O.v.x = -CO.O.v.x
        if(CO.O.pos.y<=-L+size and CO.O.v.y<=0) or (CO.O.pos.y>=L-size and CO.O.v.y>=0):
            CO.O.v.y = -CO.O.v.y
        if(CO.O.pos.z<=-L+size and CO.O.v.z<=0) or (CO.O.pos.z>=L-size and CO.O.v.z>=0):
            CO.O.v.z = -CO.O.v.z
    for CO in COs: 
        totalcomk+= CO.com_K()*dt    
        totalvk += CO.v_K()*dt
        totalvp += CO.v_P()*dt
        totalrk += CO.r_K()*dt 
    
    t+=dt
    times +=1
    c_avg_com_K.plot(pos = (t,totalcomk/t))
    c_avg_v_P.plot(pos = (t,totalvp/t))
    c_avg_v_K.plot(pos = (t,totalvk/t))
    c_avg_r_K.plot(pos = (t,totalrk/t))