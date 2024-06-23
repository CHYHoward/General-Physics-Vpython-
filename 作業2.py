from vpython import *
g = vec(0,-9.8,0)
size = 0.2
m = 1
l = 2
k = 150000
num = 2   #input#
scene = canvas(width=600, height=600, center=vec(0, -2, 0), background=vec(0.5,0.5,0))
ceiling = box(length=4.5,height=0.01,width=0.5,color=color.blue)
oscillation1=graph(title="total of energies-t plot",width=400,height=350,xtitle="t(s)",ytitle="E(kgm^2/s^2)",align='right')
instantk=gcurve(graph=oscillation1,color=color.blue,width=4)
instantp=gcurve(graph=oscillation1,color=color.blue,width=4)
oscillation2=graph(title="averaged energy-t plot",width=400,height=350,xtitle="t(s)",ytitle="E(kgm^2/s^2)",align='right')
averagek=gcurve(graph=oscillation2,color=color.blue,width=4) 
averagep=gcurve(graph=oscillation2,color=color.blue,width=4)
totalk=0
totalp=0
t=0

def af_col_v(m1, m2, v1, v2, x1, x2): # function after collision velocity碰撞
    v1_prime = v1 + 2*(m2/(m1+m2))*(x1-x2) * dot (v2-v1, x1-x2) / dot (x1-x2, x1-x2)
    v2_prime = v2 + 2*(m1/(m1+m2))*(x2-x1) * dot (v1-v2, x2-x1) / dot (x2-x1, x2-x1)
    return (v1_prime, v2_prime)

balls = []
for i in range(num):
    ball = sphere(pos = vec((0.4*i)-sqrt(2*2-1.95*1.95),-1.95+m*g.y/k, 0), radius = size, color=color.white)
    ball.v = vec(0,0,0)
    ball.m = m
    balls.append(ball)
for i in range(num,5):
    ball = sphere(pos = vec(0.4*i,-l+m*g.y/k, 0), radius = size, color=color.white)
    ball.v = vec(0,0,0)
    ball.m = m
    balls.append(ball)
springs =[]
for i in range(5):
    spring = cylinder(pos = vec(0.4*i,0, 0), radius=0.05, thickness =0.01)
    spring.axis = balls[i].pos-spring.pos
    spring.k = k
    springs.append(spring)



dt = 0.0001
while True:
    rate(5000)
    t+=dt
    kinetic=0
    potential=0
    for i in range(5):
        springs[i].axis = balls[i].pos - springs[i].pos # new: extended from spring endpoint to ball檢檢運動
        spring_force = - k * (mag(springs[i].axis) - l) * springs[i].axis.norm() # to get spring force vector
        balls[i].a = g + spring_force / m # ball acceleration = - g in y + spring force /m
        balls[i].v += balls[i].a*dt
        balls[i].pos += balls[i].v*dt
        kinetic += 1/2*m*(mag(balls[i].v)**2)
        potential += -(m*g.y*(balls[i].pos.y-(-l)))
    instantk.plot(pos=(t,kinetic)) 
    instantp.plot(pos=(t,potential))        
    totalk+=kinetic
    totalp+=potential   
    averagek.plot(pos=(t,totalk/t))
    averagep.plot(pos=(t,totalp/t))
    
    for i in range(4):
        if (mag(balls[i].pos - balls[i+1].pos) <= 2*size and dot(balls[i].pos-balls[i+1].pos, balls[i].v-balls[i+1].v) <= 0) :
            (balls[i].v, balls[i+1].v) = af_col_v (balls[i].m, balls[i+1].m, balls[i].v, balls[i+1].v, balls[i].pos, balls[i+1].pos)








