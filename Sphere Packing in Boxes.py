#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Apr 2021 **********************************
#*******************************************************************************
from vpython import *
import numpy as np

#---------------------- Scene Information -----------------------
scene = canvas()
scene.range = 40
scene.height = 900
scene.width = 1900
scene.up = vector(0,0,1) #Z-Up for Life!
scene.forward = vector(-1,-1,-1)
scene.fov = pi/6

#---------------------- Changeable Info -------------------------
Box_Length = 8 #cm
Box_Width = 8  #cm
Box_Height = 8 #cm

Ball_Diameter = 4 #cm (Standard Ping Pong Ball = 4 cm)
Ball_Color = color.orange

#---------------------- Draws Box -------------------------------
Container = box( pos = vector( Box_Length/2 , Box_Width/2 , Box_Height/2 ),
                 size = vector( Box_Length , Box_Width , Box_Height ) ,
                 opacity = 0.3 )
scene.center = Container.pos

#---------------------- Draws Balls -----------------------------
R = Ball_Diameter / 2
X_Range = arange( R , Box_Length + R , 2*R )
Y_Range = arange( R , Box_Width + R , 2*R )
Z_Range = arange( R , Box_Height + R , sqrt(2)*R   )

Num_of_Balls = 0
for z in Z_Range:
    for y in Y_Range:
        for x in X_Range:
            #Defines Modifiers for Levels along z-axis
            if int( z / ( sqrt(2)*R ) ) % 2 == 0:
                x_mod = 0
                y_mod = 0
            else:
                x_mod = R
                y_mod = R
            #Defines Position Vector
            Ball_Pos = vector( x + x_mod , y + y_mod , z )
            #Counts and Displays Balls only if Inside Box
            if Ball_Pos.x + R <= Box_Length and Ball_Pos.y + R <= Box_Width  and Ball_Pos.z + R <= Box_Height:
                Num_of_Balls += 1
                sphere( pos = Ball_Pos , radius = R ,
                        color = Ball_Color , shininess = 0)

#---------------------- Displays Results ------------------------
print( "Number of Balls: " , Num_of_Balls )

Volume_of_Balls = 4/3 * pi * R**3 * Num_of_Balls
Volume_of_Box = Box_Length * Box_Width * Box_Height
Density = Volume_of_Balls / Volume_of_Box * 100
print( "Packing Density: " , round(Density,1) , "%" )
