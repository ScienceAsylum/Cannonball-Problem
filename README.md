# An Exploration of Sphere Packing
What's the best way to stack cannonballs on a ship deck? How many Earth's <i>actually</i> fit in the Sun? What effect do atomic bonds have on the volume of a solid? All of this depends on how spheres are packed. No matter what, there will be space between them. However, that space can be minimized with a proper packing technique.

## Necessary Software
They're all coded in Python 3.8 using the Visual Python 7 (vpython) package. If you haven't already, install Python then type the following into your command line to add the vpython package:

```
pip install vpython --upgrade
```

## There Are Several Different Programs

### Ball Stacks
Starting with the original cannonball problem from 1587 CE, what shape is best for the base of the stack? I've included a 3D model for each case (<a href="https://github.com/ScienceAsylum/Cannonball-Problem/blob/main/Cannonball_Stack_Triangle_Base.py">triangle</a>, <a href="https://github.com/ScienceAsylum/Cannonball-Problem/blob/main/Cannonball_Stack_Square_Base.py">square</a>, and <a href="Cannonball_Stack_Hexagon_Base.py">hexagon</a>). Just run the program and use the mouse to control the camera. (Note: Make sure you've downloaded the <a href="https://github.com/ScienceAsylum/Cannonball-Problem/blob/main/Cannonball_Floor.png">floor texture</a> for these programs.)

The downside to VPython is that it's not very good at ray tracing, so there's no shadow cast on the floor. I hope that gets fixed eventually.

### Packing Spheres in a Box
Before running the <a href="https://github.com/ScienceAsylum/Cannonball-Problem/blob/main/Packing_Spheres_in_Boxes.py">program</a>, you can change the dimensions of the box and the size (and color) of the balls. My IRL ping pong balls were orange, but they can be any color.

```ruby
#---------------------- Changeable Info -------------------------
Box_Length = 8 #cm
Box_Width = 8  #cm
Box_Height = 8 #cm

Ball_Diameter = 4 #cm (Standard Ping Pong Ball = 4 cm)
Ball_Color = color.orange
```

Then, run the program to see the balls inside a box. Exciting! (He says sarcastically.) The program will also calulate and print the packing efficiency (as a percentage of volume filled).

### Packing Spheres in a Larger Sphere
Before running the <a href="https://github.com/ScienceAsylum/Cannonball-Problem/blob/main/Packing_Spheres_in_Spheres.py">program</a>, you can change the size of the spherical container as well as the size, texture, and color of the balls. My IRL beads were light blue, but they can be any color.

```ruby
#---------------------- Changeable Info -------------------------
Bag_Diameter = 100 #mm

Ball_Diameter = 1 #mm
Ball_Texture = textures.rough
Ball_Color = vector(0,0.5,1) #light blue
```

Then, run the program to see the balls stack in a spherical shape. The program will also calulate and print the packing efficiency (as a percentage of volume filled).

The program only displays the outermost layers of balls because I found that it stalls when there are too many balls on the screen. Some of these packs get up near a million balls. I can assure you that, while it doesn't <i>display</i> them all, it does include all of them in the efficiency calculation. Note: If your container is too small, then it won't give you optimal packing.

## Motivation for the Project
This project began when I made the following educational YouTube video:

<a href="https://youtu.be/Ga0TKrylnXY">
    <b>I proved 1,300,000 Earths WON'T fit in the Sun.</b></br>
    <img src="https://img.youtube.com/vi/Ga0TKrylnXY/mqdefault.jpg">
</a>

## License
This code is under the <a href="https://github.com/ScienceAsylum/Cannonball-Problem/blob/main/LICENSE">GNU General Public License v3.0</a>.
