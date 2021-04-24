#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Apr 2021 **********************************
#*******************************************************************************
from vpython import *
import numpy as np

#--------------------- Scene Information -----------------------
scene = canvas()
scene.range = 5
scene.height = 900
scene.width = 1900
scene.up = vector(0,0,1) #Z-Up for Life!
scene.forward = vector(-1,-1,-1)
scene.fov = pi/6

#---------------------- Object Creation ------------------------
Ground = box( pos = vector(0,0,0) , size = vector(20,0.1,20) ,
              axis = vector(1,0,0) , up = vector(0,0,1) ,
              texture = 'Cannonball_Floor.png' )

Ball_Texture = { 'file':textures.rough , 'bumpmap':bumpmaps.stucco }
Ball_Color = color.gray(0.3)
R = 0.5
Balls = []
for ele in arange(0,11,1):
    Ball = sphere( radius = R , color = Ball_Color ,
                   texture = Ball_Texture , shininess = 0 )
    Balls.append( Ball )

#Positon Level 1
Balls[0].pos = vector( 0 , 0 , 0 )
Balls[1].pos = vector( 2*R , 0 , 0 )

Balls[2].pos = rotate(Balls[1].pos, angle=pi/3, axis=scene.up)
Balls[3].pos = rotate(Balls[1].pos, angle=2*pi/3, axis=scene.up)
Balls[4].pos = rotate(Balls[1].pos, angle=pi, axis=scene.up)
Balls[5].pos = rotate(Balls[1].pos, angle=4*pi/3, axis=scene.up)
Balls[6].pos = rotate(Balls[1].pos, angle=5*pi/3, axis=scene.up)

#Positon Level 2
Balls[7].pos = vector( -R , -sqrt(3)*R/3 , 2*sqrt(6)*R/3 )
Balls[8].pos = vector( R , -sqrt(3)*R/3 , 2*sqrt(6)*R/3 )

Balls[9].pos = vector( 0 , 2*sqrt(3)*R/3 , 2*sqrt(6)*R/3 )

#Positon Level 3
Balls[10].pos = vector( 0 , 0 , 4*sqrt(6)*R/3 )

#Shift Floor
Ground.pos.z -= Ground.height/2 + R
