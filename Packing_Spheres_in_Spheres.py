#*******************************************************************************
#**************************** Created by Nick Lucid ****************************
#*********************************** Apr 2021 **********************************
#*******************************************************************************
from vpython import *
import numpy as np

#---------------------- Scene Information ----------------------
scene = canvas()
scene.range = 80
scene.height = 1080
scene.width = 1920
scene.up = vector(0,0,1) #Z-Up for Life!
scene.forward = vector(-1,-1,-1)
scene.fov = pi/6

#---------------------- Changeable Info -------------------------
Bag_Diameter = 100 #mm

Ball_Diameter = 1 #mm
Ball_Texture = textures.rough
Ball_Color = vector(0,0.5,1) #light blue

#---------------------- Draws Bag -------------------------------
Bag = sphere( pos = Bag_Diameter/2 * vector(1,1,1) ,
              radius = Bag_Diameter/2 , opacity = 0.3 ,
              color = color.yellow , visible = 0 )
scene.center = Bag.pos

#---------------------- Draws Balls -----------------------------
R = Ball_Diameter / 2
X_Range = arange( -2*R , Bag_Diameter + 2*R , 2*R )
Y_Range = arange( -2*R , Bag_Diameter + 2*R , 2*R )
Z_Range = arange( -2*R , Bag_Diameter + 2*R , sqrt(2)*R   )

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
            #Counts only if Inside Bag
            if mag( Ball_Pos - Bag.pos ) + R <= Bag.radius:
                Num_of_Balls += 1
            #Displays Balls only if Inside Bag and only first few layers
            if mag( Ball_Pos - Bag.pos ) + R <= Bag.radius and mag( Ball_Pos - Bag.pos ) + R >= Bag.radius - 2:
                sphere( pos = Ball_Pos , radius = R ,
                        axis = vector(-1,-1,0) , up = vector(0,0,1) ,
                        texture = Ball_Texture , color = Ball_Color )

#---------------------- Displays Results ------------------------
print("Number of Beads: " , Num_of_Balls)

Volume_of_Balls = 4/3 * pi * R**3 * Num_of_Balls
Volume_of_Bag = 4/3 * pi * Bag.radius**3
print("Packing Density: " , Volume_of_Balls/Volume_of_Bag)
