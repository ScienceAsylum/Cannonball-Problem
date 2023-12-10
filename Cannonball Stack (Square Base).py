#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Apr 2021 **********************************
#*******************************************************************************
from vpython import *
import numpy as np

#--------------------- Scene Information -----------------------
scene = canvas()
scene.range = 5
scene.height = 1080
scene.width = 1920
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
for ele in arange(0,14,1):
    Ball = sphere( radius = R , color = Ball_Color ,
                   texture = Ball_Texture , shininess = 0 )
    Balls.append( Ball )

#Positon Level 1
Balls[0].pos = vector( -2*R , -2*R , 0 )
Balls[1].pos = vector( -2*R , 0 , 0 )
Balls[2].pos = vector( -2*R , 2*R , 0 )

Balls[3].pos = vector( 0 , -2*R , 0 )
Balls[4].pos = vector( 0 , 0 , 0 )
Balls[5].pos = vector( 0 , 2*R , 0 )

Balls[6].pos = vector( 2*R , -2*R , 0 )
Balls[7].pos = vector( 2*R , 0 , 0 )
Balls[8].pos = vector( 2*R , 2*R , 0 )

#Positon Level 2
Balls[9].pos = vector( -R , -R , sqrt(2)*R )
Balls[10].pos = vector( -R , R , sqrt(2)*R )

Balls[11].pos = vector( R , -R , sqrt(2)*R )
Balls[12].pos = vector( R , R , sqrt(2)*R )

#Positon Level 3
Balls[13].pos = vector( 0 , 0 , 2*sqrt(2)*R )

#Shift Floor
Ground.pos.z -= Ground.height/2 + R
