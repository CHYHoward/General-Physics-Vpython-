
from vpython import *
G = 6.673E-11
mass = {'earth':5.97E24,'moon':7.36E22,'sun':1.99E30}
radius = {'earth':6.371E6*10,'moon':1.317E6*10,'sun':6.95E8*10}
earth_orbit = {'r':1.495E11,'v':2.9783E4}
moon_orbit = {'r':3.84E8,'v':1.022E3}
theta = 5.145*pi/180.0
dt = 60*60*6
def G_force(m1,m2,pos_vec):
    return -G*m1*m2/mag2(pos_vec)*norm(pos_vec)
class as_obj(sphere):
    def kinetic_energy(self):
        return 0.5*self.m*mag2(self.v)
    
scene = canvas(width=800, height=800,background=vector(0.5,0.5,0))
scene.lights = []

sun = sphere(pos=vector(0,0,0), radius = 3.0E10, color = color.orange, emissive=True)
local_light(pos = vector(0,0,0))
earth = as_obj(pos = mass['moon']/(mass['moon']+mass['earth'])*moon_orbit['r']*vector(-cos(theta),sin(theta),0)+vector(earth_orbit['r'],0,0),radius = radius['earth'],m = mass['earth'],texture=textures.earth)
moon = as_obj(pos = mass['earth']/(mass['moon']+mass['earth'])*moon_orbit['r']*vector(cos(theta),-sin(theta),0)+vector(earth_orbit['r'],0,0),radius = radius['moon'],m = mass['moon'])
moon.v = mass['earth']/(mass['moon']+mass['earth'])*moon_orbit['v']* vector(0,0,-1)+vector(0,0,-earth_orbit['v'])
earth.v = mass['moon']/(mass['moon']+mass['earth'])*moon_orbit['v']* vector(0,0,1)+vector(0,0,-earth_orbit['v'])
n_vec = arrow(color = color.white,shaftwidth = 4E6)

t = 0
timing = True

while True:
    
    rate(1000)
    
    force = G_force(mass['moon'],mass['earth'],moon.pos-earth.pos)
    moon.a = (force+G_force(mass['moon'],mass['sun'],moon.pos))/moon.m
    moon.v = moon.v+moon.a*dt
    moon.pos = moon.pos+moon.v*dt
    earth.a = (-force+G_force(mass['earth'],mass['sun'],earth.pos))/earth.m
    earth.v = earth.v+earth.a*dt
    earth.pos = earth.pos + earth.v*dt

    n_vec.pos = earth.pos
    direct = norm(cross(moon.pos-earth.pos,moon.v-earth.v))
    n_vec.axis = 3E8*direct
    if n_vec.axis.x <0:
       t+=dt
    if t != 0 and n_vec.axis.x>=0 and timing:
       print(2*t/86400/365.25)
       timing = False
       t = 0
    scene.center = earth.pos
     

 
