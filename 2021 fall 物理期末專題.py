from vpython import*

c = 3 * 10**8

L = 4000
real_arm1 = L
real_arm2 = L

light_start_pos1 = vec(0,0,0)
light_start_pos2 = vec(0,0,0)
real_beam1_pos = light_start_pos1
real_beam2_pos = light_start_pos2

light_start_v1 = vec(0,c,0)
light_start_v2 = vec(c,0,0)
real_beam1_v = light_start_v1
real_beam2_v = light_start_v2

g_wave_amp = 1E-2
g_wave_omega = 2*pi*100
light_omega = 2*pi*10E6

Em_graph = graph(xtitle = "t",ytitle = "Em",align = 'left') 
Em = gcurve(color = color.cyan,graph = Em_graph) # Em -- time graph
G_wave_graph = graph(xtitle = "t",ytitle = "Displacement",align = 'left') 
G_wave = gcurve(color = color.red,graph = G_wave_graph)
G_wave_real = gcurve(color = color.green,graph = G_wave_graph)

light_dt = 1E-10

light_t = 0
pre_time = light_t
t_initial = 5E-4

displacement = -0.5 * c/(light_omega/2/pi)

over_19 = True
Em_max = 0.90
epsi = 1E-10

while True:
    #rate(10000)
    
    # real interference of light_beam
    #light_t += light_dt
    #real_beam1_pos.y += real_beam1_v.y * light_dt
    #real_beam2_pos.x += real_beam2_v.x * light_dt
    if light_t >= t_initial:
        real_arm2 = L * (1 + g_wave_amp * sin(g_wave_omega * (light_t - t_initial))) #simulated g_wave

    #if real_beam1_pos.y >= L and real_beam1_v.y > 0: #beam1 hits the upper mirror
     #   real_beam1_v = -real_beam1_v
        
    #if real_beam2_pos.x >= real_arm2 and real_beam2_v.x > 0: #beam2 hits the right mirror
     #   real_beam2_v = -real_beam2_v
       
    #if real_beam1_pos.y <= 0  and real_beam1_v.y < 0:
    light_t = c/L*2
    E_beam1 = cos(light_omega * light_t)
    circle = light_omega*light_t // (2*pi)  # 0 <= phi <= 2pi
    phi_1 = light_omega*light_t - circle * 2*pi
    real_beam1_v = vec(0,0,0)
        
    #if real_beam2_pos.x <= 0  and real_beam2_v.x < 0:
    light_t = c/real_arm2*2
    E_beam2 = cos(light_omega * light_t)
    circle = light_omega*light_t // (2*pi)
    phi_2 = light_omega*light_t - circle* (2*pi)
    real_beam2_v = vec(0,0,0)
        
    #if real_beam1_v == vec(0,0,0) and real_beam2_v == vec(0,0,0):
    if abs(phi_1-phi_2) <= pi:
        Em_combined = 2 * cos(abs(phi_1 - phi_2)/2) # magnitude of combined E_field
    if abs(phi_1-phi_2) > pi:
        Em_combined = 2 * cos(pi-abs(phi_1 - phi_2)/2)
    real_beam1_pos = light_start_pos1
    real_beam2_pos = light_start_pos2
    real_beam1_v = light_start_v1
    real_beam2_v = light_start_v2
       
    Em.plot(light_t,Em_combined)

    if over_19 == False and Em_combined <= Em_max:
        over_19 = True
    if cos(g_wave_omega * light_t ) >= 0 and Em_combined >= Em_max  and over_19 == True:  # redshift
        over_19 = False
        displacement += 0.5 * c/(light_omega/2/pi)
    if cos(g_wave_omega * light_t) < 0 and Em_combined >= Em_max  and over_19 == True:  # blueshift
        over_19 = False
        displacement -= 0.5 * c/(light_omega/2/pi)

    G_wave.plot(light_t,displacement/L)
    if light_t >= t_initial:
        G_wave_real.plot(light_t,g_wave_amp * sin(g_wave_omega * (light_t - t_initial)))
    if light_t < t_initial:
        G_wave_real.plot(light_t,0)