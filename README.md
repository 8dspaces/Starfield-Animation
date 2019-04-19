# Starfield Animation in python
This script uses `tkinter`'s `canvas` to draw stars, like in those awesome old demos. This script doesn't use any game engines.

### Requirements
Python 3+ and numpy

### Principle
The thoery behind this animation is pretty simple.
  - Generate random coordinates of stars (x,y,z)
  - z is the depth, a measure of how far the star is
  - Move stars such that next position is a function of depth. This essentially means, considering our stars moving in y axis: `new y = old y + depth`. If you want horizontal motion, you can replace y by x.
  - Set this event of drawing and moving stars in a loop
 
 ### Screenshot
![Starfield](https://i.imgur.com/GFAfzSO.png)

Have fun!
