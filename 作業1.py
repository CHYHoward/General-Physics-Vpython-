from vpython import*
g=9.8
size=0.25
height=15.0
C_drag=0.9
theta=pi/4
scene=canvas(width=800,height=800,center=vec(0,height/2,0),background=vec(0.5,0.5,0))
floor=box(length=100,height=0.01,width=10,color=color.blue)
ball=sphere(radius=size,color=color.red,make_trail=True,trail_radius=0.2)

a1=arrow(color=color.green,shaftwidth=0.05)

ball.pos=vec(-15,size,0)
ball.v=vec(20*cos(theta),20*sin(theta),0)
displacement=vec(0,0,0)
oscillation=graph(title="v-t plot",width=600,height=450,x=0,y=600,xtitle="t(s)",ytitle="v(m/s)",alighn='right')
funct1=gcurve(graph=oscillation,color=color.blue,width=4)

a1.pos=ball.pos
a1.axis=ball.v*0.5

t=0
dt=0.001
i=0

path=0
largest_height=0


while ball.pos.y>=size and  i<3:
    rate(1000)
    ball.v=ball.v-vec(0,g,0)*dt-C_drag*ball.v*dt
    ball.pos+=ball.v*dt
    a1.pos=ball.pos
    a1.axis=ball.v
    path+=((ball.v*dt).mag)

    funct1.plot(pos=(t,mag(ball.v)))
    t+=dt

    if ball.v.y<=0 and ball.pos.y> largest_height:

        largest_height=ball.pos.y

    if ball.pos.y<=size and ball.v.y<0:
        ball.v.y=-ball.v.y
        ball.pos+=ball.v*dt
        i+=1

displacement=ball.pos-vec(-15,size,0)
msg=text(text='The largest height = '+str(largest_height),pos=vec(0,15,0))
msg=text(text='The displacement of the ball = '+str(mag(displacement)),pos=vec(0,16,0))
msg=text(text='The total distance travelled by the ball = '+str(path),pos=vec(0,17,0))
