from vpython import*
R = 0.12
r = 0.06
u = 4*pi*10**(-7)
I = 1


d_theta = 2*pi/1000

#-----------------------大園對小圓---------------
dr = r/1000
flux1 = 0
for i in range (1000):
    B1 = vector(0,0,0)
    k1 = i*dr+dr/2#圓弧半徑
    for j in range(1000):
        s1 = R*vector(cos(d_theta*j),sin(d_theta*j),0)
        ds1 = R*d_theta*vector(-sin(d_theta*j),cos(d_theta*j),0)
        p1 = vector(k1,0,0.1)
        r_vec = p1-s1
        r_norm = r_vec.norm()
        t = 4*pi*(mag(r_vec))**2
        dB = u*I*(ds1.cross(r_norm))/t
        B1+=dB
    A1 = pi*(k1+dr/2)**2
    A2 = pi*(k1-dr/2)**2
    dA = (A1-A2)*vector(0,0,1)
    flux1 += B1.dot(dA)

print(flux1)

#---------------------小圓對大園---------------

dR = R/1000
flux2 = 0
for i in range (1000):
    B2 = vector(0,0,0)
    k2 = i*dR+dR/2
    for j in range(1000):
        s2 = vector(r*cos(d_theta*j),r*sin(d_theta*j),0.1)
        ds2 = r*d_theta*vector(-sin(d_theta*j),cos(d_theta*j),0)
        p2 = vector(k2,0,0)
        r_vec = p2-s2
        r_norm = r_vec.norm()
        t = 4*pi*(mag(r_vec))**2
        dB = u*I*(ds2.cross(r_norm))/t
        B2+=dB
    A3 = pi*(k2+dR/2)**2
    A4 = pi*(k2-dR/2)**2
    dA = (A3-A4)*vector(0,0,1)
    flux2 += B2.dot(dA)

print(flux2)