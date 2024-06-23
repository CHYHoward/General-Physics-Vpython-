from vpython import*

c = 3 * 10E8
L = 10
real_arm1 = L
real_arm2 = L
light_start = vec(-8,-10,0) # let light starts at the middle of beam_splitter
light_start_pos1 = vec(-10,-10,0)
light_start_pos2 = vec(-10,-10,0)
real_beam1_pos = light_start_pos1
real_beam2_pos = light_start_pos2

light_start_v1 = vec(0,c,0)
light_start_v2 = vec(c,0,0)
real_beam1_v = light_start_v1
real_beam2_v = light_start_v2

g_wave_amp = 0.1
g_wave_omega = 100*2*pi
light_omega = 2*pi*10E8

Em_graph = graph(xtitle = "t",ytitle = "Em",align = 'left') 
Em = gcurve(color = color.cyan,graph = Em_graph) # Em -- time graph

scene = canvas(width=1000, height=500, background=vector(0.5,0.5,0.5), align = 'right')
light_source = arrow(shaftwidth=1,headwidth=2,headlength=3,axis=vector(5,0,0),pos=vec(-15,-10,0))

arm1 = box(size=vec(0.2,L,0.01), pos=vec(-10,-5,0), color = color.blue)
arm2 = box(size=vec(L,0.2,0.01), pos=vec(-5,-10,0), color = color.blue)
beam_splitter = arrow(axis=vec(4,4,0),pos=vec(-12,-12,0),shaftwidth=0.4,headwidth=0.4,headlength=0.01,color=color.red)
mirror1 = box(size=vec(3,0.2,0.01), pos=vec(-10,0,0), color = color.red)
mirror2 = box(size=vec(0.2,3,0.01), pos=vec(0,-10,0), color = color.red)
#only for demonstrating the path
light_beam1 = sphere(radius=0.5,color=color.yellow,pos=vec(-10,-10,0))
light_beam2 = sphere(radius=0.5,color=color.yellow,pos=vec(-10,-10,0))
screen = box(size = vec(3,0.2,0.01), pos = vec(-10,-12,0), color = color.black)

ball_speed = 2
ball_start_v = vec(ball_speed,0,0)
light_beam1.v = ball_start_v
light_beam2.v = ball_start_v


ball_dt = 10E-4
ball_t = 0
ball_period = 0 
ball_stop = False # if ball_stop = true, balls are static



while True:

    # virtual balls
    ball_t += ball_dt
    if ball_t >= 5*ball_period and ball_period != 0 and ball_stop == True:
        #balls stop for 5 period after running for a period
        sleep(0.1)
        ball_stop = False
        ball_t = 0
        light_beam1.pos = vec(-10,-10,0)
        light_beam2.pos = vec(-10,-10,0)
        light_beam1.v = ball_start_v
        light_beam2.v = ball_start_v
        
    if ball_stop == False:
        rate(10000)
        light_beam1.pos += light_beam1.v * ball_dt
        light_beam2.pos += light_beam2.v * ball_dt
        arm2.size.x = L + 20 * g_wave_amp * sin(g_wave_omega/1000 * ball_t) # visible arm contract
        arm2.pos.x = -10 + 0.5 * (L + 20 * g_wave_amp * sin(g_wave_omega/1000 * ball_t))
        mirror2.pos.x = arm2.pos.x + arm2.length/2
        
        if light_beam1.pos.x >= -10 and light_beam1.v.x > 0: #beam1 hits the beam_splitter 
            light_beam1.v = vec(0,ball_speed,0)
            
        if light_beam1.pos.y >= 0 and light_beam1.v.y > 0: #beam1 hits the upper mirror
            light_beam1.v = -light_beam1.v
            
        if light_beam2.pos.x >= 0  and light_beam2.v.x > 0: #beam2 hits the right mirror
            light_beam2.v = -light_beam2.v
            
        if light_beam2.pos.x <= -10 and light_beam2.v.x < 0: #beam2 hits the beam_splitter
            light_beam2.v = vec(0,-ball_speed,0)
            
        if light_beam1.pos.y <= -12 and light_beam1.v.y < 0: #beam1 arrives the screen
            light_beam1.v = vec(0,0,0)
            
        if light_beam1.pos.y <= -12 and light_beam2.pos.y <= -12:
            #both beams arrives the screen and turn back to the lightsource
            ball_stop = True  
            ball_period = ball_t
            ball_t = 0
            #sleep(0.1)
            
        
    # real interference of light_beam
   
        