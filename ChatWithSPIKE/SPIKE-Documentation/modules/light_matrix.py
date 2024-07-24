functions = {
    "clear": """
clear() -> None

Switches off all of the pixels on the Light Matrix.


from hub import light_matrix
import time
# Update pixels to show an image on Light Matrix, and then turn them off using the clear function 

# Show a small heart 
light_matrix.show_image(2)

# Wait for two seconds 
time.sleep_ms(2000)

# Switch off the heart 
light_matrix.clear()
""",

    "get_orientation": """
get_orientation() -> int

Retrieve the current orientation of the Light Matrix.
Can be used with the following constants: orientation.UP, orientation.LEFT, orientation.RIGHT, orientation.DOWN
""",

    "get_pixel": """
get_pixel(x: int, y: int) -> int

Retrieve the intensity of a specific pixel on the Light Matrix.


from hub import light_matrix

# Show a heart 
light_matrix.show_image(1)

# Print the value of the centre pixel's intensity 
print(light_matrix.get_pixel(2, 2))
Parameters
x: int
The X value, range (0 - 4)

y: int
The Y value, range (0 - 4)
""",

    "set_orientation": """
set_orientation(top: int) -> int

Change the orientation of the Light Matrix. All subsequent calls will use the new orientation.
Can be used with the following constants: orientation.UP, orientation.LEFT, orientation.RIGHT, orientation.DOWN

Parameters
top: int
The side of the hub to be the top
""",

    "set_pixel": """
set_pixel(x: int, y: int, intensity: int) -> None

Sets the brightness of one pixel (one of the 25 LEDs) on the Light Matrix.

from hub import light_matrix

# Turn on the pixel in the centre of the hub 
light_matrix.set_pixel(2, 2, 100)
Parameters
x: int
The X value, range (0 - 4)

y: int
The Y value, range (0 - 4)

intensity: int
How bright to light up the pixel
""",

    "show": """
show(pixels: list[int]) -> None

Change all the lights at the same time.


from hub import light_matrix
# Update all pixels on Light Matrix using the show function 

# Create a list with 25 identical intensity values 
pixels = [100] * 25 

# Update all pixels to show same intensity 
light_matrix.show(pixels)
Parameters

pixels: Iterable
A list containing light intensity values for all 25 pixels.
""",

    "show_image": """
show_image(image: int) -> None

Display one of the built-in images on the display.

from hub import light_matrix
# Update pixels to show an image on Light Matrix using the show_image function 

# Show a smiling face 
light_matrix.show_image(light_matrix.IMAGE_HAPPY)
Parameters
image: int
The id of the image to show. The range of available images is 1 to 67. There are constants in the light_matrix module for these.
""",

    "write": """
write(text: str, intensity: int = 100, time_per_character: int = 500) -> Awaitable

Displays text on the Light Matrix, one letter at a time, scrolling from right to left, except if there is a single character to show (which will not scroll)

from hub import light_matrix
# White a message to the hub 
light_matrix.write("Hello, world!")
Parameters
text: str
The text to display

intensity: int
How bright to light up the pixel

time_per_character: int
How long to show each character on the display
"""
}