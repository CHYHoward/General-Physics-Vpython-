from vpython import*

fd = 120 # 120Hz
#(Your Parameters here)
R = 30
L = 200E-3
C = 20E-6
t = 0
dt = 1.0/(fd * 5000) # 5000 simulation points per cycle
scene1 = graph(align = 'left', xtitle='t', ytitle='i (A) blue, v (100V) red,', background=vector(0.2, 0.6, 0.2))
scene2 = graph(align = 'left', xtitle='t', ytitle='Energy (J)', background=vector(0.2, 0.6, 0.2))
i_t = gcurve(color=color.blue, graph = scene1)
v_t = gcurve(color=color.red, graph = scene1)
E_t = gcurve(color=color.red, graph = scene2)

v,v_c,v_l = 0,0,0
E = 0
i = 0

prev_i ,prevprev_i = 0,0
count = 0

E_10percent_t = 0
E_10percent_Mag = 0

nineth_T = 0
nineth_Mag = 0

while t<=(20/fd):
    rate(5000)

    if t <(12/fd):
        v = 36*sin(2*pi*fd*t)
    else:
        v = 0

    v_l = v-v_c-i*R
    i += (v_l/L)*dt
    v_c += (i/C)*dt
    E = 0.5*C*v_c**2+0.5*L*i**2
    t+=dt

    if(count < 9):
        if(prev_i-prevprev_i > 0 and prev_i-i > 0):
            count+=1

        if(count == 9):
            nineth_T = (t-dt)*fd
            nineth_Mag = prev_i
            print("Magnitude of i")
            print("Numerical Value:",nineth_Mag,"Theoretical Value:",36/sqrt((30)**2+(48*pi-10000/(48*pi))**2))
            
            print("Phase constant of i")
            print("Numerical Value:",2*pi*(floor(nineth_T)+0.25-nineth_T),"Theoretical Value:",atan(-(48*pi-10000/(48*pi))/30))
            
        prevprev_i = prev_i
        prev_i = i

    if t>=(12/fd):
        if E_10percent_Mag == 0:
            E_10percent_Mag = 0.1*E
        if E <= E_10percent_Mag and (E_10percent_t == 0):
            E_10percent_t = t
            print("The energy drops below 0.1E(t=12T) at t=",t)


    v_t.plot(pos=(t*fd,v/100))
    i_t.plot(pos=(t*fd,i))
    E_t.plot(pos=(t*fd,E))
