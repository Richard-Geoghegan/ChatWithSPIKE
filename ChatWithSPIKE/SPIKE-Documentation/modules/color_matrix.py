functions = {
    "clear": """
clear(port: int) -> None

Turn off all pixels on a Colour Matrix


from hub import port
import color_matrix

color_matrix.clear(port.A)
Parameters
port: int
A port from the port submodule in the hub module
""",

    "get_pixel": """
get_pixel(port: int, x: int, y: int) -> tuple[int, int]

Retrieve a specific pixel represented as a tuple containing the colour and intensity


from hub import port
import color_matrix

# Print the colour and intensity of the 0,0 pixel on the Colour Matrix connected to port A 
print(color_matrix.get_pixel(port.A, 0, 0))
Parameters
port: int
A port from the port submodule in the hub module

x: int
The X value (0 - 2)

y: int
The Y value, range (0 - 2)
""",

    "set_pixel": """
set_pixel(port: int, x: int, y: int, pixel: tuple[color: int, intensity: int]) -> None

Change a single pixel on a Colour Matrix


from hub import port
import color
import color_matrix

# Change the colour of the 0,0 pixel on the Colour Matrix connected to port A 
color_matrix.set_pixel(port.A, 0, 0, (color.RED, 10))

# Print the colour of the 0,0 pixel on the Colour Matrix connected to port A 
print(color_matrix.get_pixel(port.A, 0, 0)[0])
Parameters
port: int
A port from the port submodule in the hub module

x: int
The X value (0 - 2)

y: int
The Y value, range (0 - 2)

pixel: tuple[color: int, intensity: int]
Tuple containing colour and intensity, meaning how bright to light up the pixel
""",

    "show": """
show(port: int, pixels: list[tuple[int, int]]) -> None

Change all pixels at once on a Colour Matrix


from hub import port
import color
import color_matrix

# Update all pixels on Colour Matrix using the show function 

# Create a list with 18 items (colour and intensity pairs) 
pixels = [(color.BLUE, 10)] * 9 

# Update all pixels to show same colour and intensity 
color_matrix.show(port.A, pixels)
Parameters
port: int
A port from the port submodule in the hub module

pixels: list[tuple[int, int]]
A list containing colour and intensity value tuples for all 9 pixels.
"""
}