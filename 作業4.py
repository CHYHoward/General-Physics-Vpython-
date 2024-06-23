import numpy as np
from vpython import *
A, N, omega = 0.10,50,2*pi/1.0
size ,m,k,d = 0.06,0.1,10.0,0.4

scene = graph(title='Phonon dispersion relationship', width=800, height=300, background=vec(0.5,0.5,0), center = vec((N-1)*d/2, 0, 0))

p = gcurve(color = color.blue,graph = scene)
Unit_K = 2 * pi/(N*d)

for i in range(1,int(N/2-1)):
    rate(10000)
    Wavevector =  i * Unit_K
    phase = Wavevector * arange(N) * d
    ball_pos, ball_orig, ball_v, spring_len = np.arange(N)*d + A*np.sin(phase),np.arange(N)* d, np.zeros(N), np.ones(N)*d
    
    t = 0
    dt = 0.0003
    
    while (ball_pos[1] - d) > -A*np.sin(phase[1]):
        t += dt
        
        spring_len[:-1] = ball_pos[1:] - ball_pos[:-1]
        spring_len[-1] = N * d + ball_pos[0] - ball_pos[-1]
        ball_v[1:] += (k*(spring_len[1:]-d)-k*(spring_len[:-1]-d))/m*dt
        ball_v[0] += (k*(spring_len[0]-d)-k*(spring_len[-1]-d))/m*dt
        ball_pos += ball_v*dt

    period = 2*t
    angular_frequency = 2*pi/period        
    p.plot(pos = (Wavevector,angular_frequency))